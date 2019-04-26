import urllib.request as ur
import re
import random
import pymysql
import datetime
from threading import Timer
from bs4 import BeautifulSoup as bs
import json
import time

# 浏览器伪装列表
user_agent_pools = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
        'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)'
]

# 斗鱼直播分类字典，key为直播分类名称，value为分类URL
classify_dict = {
    '网游竞技' : 'https://www.douyu.com/directory/index/PCgame?isAjax=1',
    '单机热游' : 'https://www.douyu.com/directory/index/djry?isAjax=1',
    '手游休闲' : 'https://www.douyu.com/directory/index/syxx?isAjax=1',
    '娱乐天地' : 'https://www.douyu.com/directory/index/yl?isAjax=1',
    '颜值'     : 'https://www.douyu.com/directory/index/yz?isAjax=1',
    '科技教育' : 'https://www.douyu.com/directory/index/kjjy?isAjax=1',
    '语音直播' : 'https://www.douyu.com/directory/index/voice?isAjax=1',
    '正能量'   : 'https://www.douyu.com/directory/index/znl?isAjax=1'
}

# 运用除法运算向上取整，来获取当前直播人数的直播列表分页数
def page_num(playNum, pageSize):
    return int((playNum + pageSize - 1) / pageSize)

# 通过urllib模块获取url的html信息
# 这里通过while循环，利用线程睡眠控制程序2秒重连，增加容错性
def open_url(url):
    # 从浏览器伪装池中随机获取一个头信息，并设置给opener对象
    user_agent = random.choice(user_agent_pools)
    headers = ('User-Agent', user_agent)
    opener = ur.build_opener()
    opener.addheaders = [headers]
    # 将opener对象设为全局
    ur.install_opener(opener)
    flag = False
    while not flag:
        try:
            # 获取html信息
            data = ur.urlopen(url).read().decode('utf-8')
        except Exception as e:
            print('url [' + url + '] HTTP请求失败！正在准备重连……')
            time.sleep(2)
            continue
        flag = True
    return data

# 通过斗鱼网站的搜索获取游戏的开播人数，偶尔会出现获取直播人数失败的情况(一天1~2次)，导致索引越界，具体原因没有明查
# 这里通过while循环，利用线程睡眠控制程序2秒重连，增加容错性
def play_search(url):
    flag = False
    while not flag:
        try:
            err_data = open_url(url)
            # 使用正则表达式匹配
            play_num = re.compile('<strong>\\s+(.*)<span>直播</span>').findall(err_data)[0]
        except IndexError as e:
            print('url [' + url + '] 获取直播人数失败！正在准备重连……')
            time.sleep(2)
            continue
        flag = True
    return play_num

# 爬虫程序
def crawl():

    # 记录该次爬取时间，为了便于后期的分析，开始爬取时记录当前的爬取时间作为该次爬取到的所有数据的爬取时间
    crawl_start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 爬取时间

    # 准备数据库连接
    db = pymysql.Connect(host="127.0.0.1", user="root", password="123456", db="crawl", port=3306)
    cur = db.cursor()
    print('连接数据库成功！开始爬取网页数据……')

    # 遍历斗鱼网站的分类字典列表，获取分类名称(key)与对应的URL(value)
    for classify in classify_dict.items():
        # 获取分类下的游戏列表
        game_list_data = open_url(classify[1])
        # 通过BeautifulSoup截取游戏列表中每个游戏对应的直播列表url和data-tid(后面有用)
        game_list = bs(game_list_data)
        # 遍历页面所有a标签，获取每个a标签里面的href、data-tid
        for i in game_list.find_all('a'):
            detail_url = "https://www.douyu.com" + str(i['href'])
            data_id = str(i['data-tid'])
            # 获取游戏直播列表html
            game_detail_data = open_url(detail_url)
            game_detail = bs(game_detail_data)
            # 获取h1标签为游戏名称
            game = game_detail.h1.text # 游戏名称
            try:
                # 获取class=play_num为开播人数
                play_num = int(game_detail.select(".play_num")[0].text) # 开播人数
                # 获取class=watch-num为观看热度
                watch_num = int(game_detail.select(".watch-num")[0].text)
                # 存在有些游戏，斗鱼在页面上没有给出该游戏的开播人数和观看热度的统计数据，会导致BeautifulSoup截取失败而抛出异常
            except Exception as e:
                # 当获取游戏的开播人数和观看热度失败时，我们自己进行统计
                # print("游戏 [" + game + "] 自动获取开播人数及热度失败, 开始自定义统计开播人数及热度")
                # 通过斗鱼网站的搜索获取某游戏来开播人数
                keyword = ur.quote(game) # 对中文进行编码
                search_url = 'https://www.douyu.com/search/?kw=' + keyword
                play_num = play_search(search_url)
                # 根据开播人数计算游戏的直播列表分页页数
                pageNum = page_num(int(play_num), 120)
                # 定义热度总和变量
                watch_num = 0
                # 获取每页的直播列表，并统计热度
                for i in range(1, pageNum + 1):
                    # 该url返回为json对象，由于有的游戏url为'1_'+data_id，有的url则为'2_'+data_id,没有发现什么规律
                    # 故这里的做法为两个url都拼起来，先查询第一个，若第一个查询结果数据长度为空，则使用第二个
                    detail_url = 'https://www.douyu.com/gapi/rkc/directory/1_' + str(data_id) + '/' + str(i)
                    # 获取json字符串
                    err_data = open_url(detail_url)
                    # 将json字符串转化为json对象
                    obj = json.loads(err_data)
                    if len(obj['data']['rl']) == 0:
                        detail_url = 'https://www.douyu.com/gapi/rkc/directory/2_' + str(data_id) + '/' + str(i)
                        err_data = open_url(detail_url)
                        obj = json.loads(err_data)
                    for j in range(0, len(obj['data']['rl'])):
                        watch_num += int(obj['data']['rl'][j]['ol'])    # 统计热度
            # 组装sql语句
            sql = "INSERT INTO douyu_crawl_data (classify_name, game_name, play_num, watch_num, crawl_time) VALUES ('" + str(classify[0]) + "','" + str(game) + "','" + str(play_num) + "','" + str(watch_num) + "','" + str(crawl_start_time) + "')"
            print(sql)
            # 执行sql语句
            cur.execute(sql)
            db.commit()

    # 关闭数据库连接
    cur.close()
    db.close()
    # 定时器，定时半小时执行爬取程序，计算整个过程一次爬取时间，1800-爬取所用时间为间隔时长
    crawl_space_time = 1800.0 - (float(int(datetime.datetime.now().timestamp())) - time.mktime(time.strptime(crawl_start_time,'%Y-%m-%d %H:%M:%S')))
    print("==========================================================================================")
    print("       爬取结束!等待下一次爬取,下一次爬取将于[" + str(crawl_space_time) + '] 秒后进行……      ')
    print("==========================================================================================")
    t = Timer(crawl_space_time, crawl)
    t.start()

if __name__ == '__main__':
    crawl()

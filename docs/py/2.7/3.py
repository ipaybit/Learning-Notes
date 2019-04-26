from urllib import request
 
url = r'https://www.baidu.com/'
headers = {
    'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
    'Connection': 'keep-alive'
}
req = request.Request(url, headers=headers)
html = request.urlopen(req).read()
 
# 处理编码
html = html.decode('utf-8')
 
print(html)

#coding:utf-8
# python2.7版本
import urllib2
 
# 设置浏览器请求头
ua_headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"
}
 
#建立请求内容
request=urllib2.Request("http://baidu.com/",headers=ua_headers)
 
#获取响应
response=urllib2.urlopen(request)
 
#页面内容
html=response.read()
 
print html
print response.getcode() #返回响应码
print response.geturl() #返回实际url
print response.info() #返回服务器响应的报头

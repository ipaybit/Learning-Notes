#!/usr/bin/python
# -*- coding : -*-
request = urllib2.Request("http://www.baidu.com/")
response = urllib2.urlopen(request)
print (response.read())

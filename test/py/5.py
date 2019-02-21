#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# 打开一个文件
fo = open("foo.txt", "w")
print "文件名: ", fo.name
 
# 关闭打开的文件
fo.close()

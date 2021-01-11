#! /usr/bin/python3
#coding=utf-8
'''
Created on Jun.10 2021
@author: kelven & duter2016
'''
import sys
import requests
from bs4 import BeautifulSoup

def main(argv):

    url = 'http://freeapi.ipip.net/'   #中文免费，免费版仅ipv4
    args = sys.argv[1]
    url=url+format(args)
    response = requests.get(url)

    str=response.text.replace('\"','') #去掉双引号
    str=str.replace('[','')            #去掉方括号
    str=str.replace(']','')
    str=str.replace(' ','')

    str=str.split(",")   #以逗号为分割符号，分割字符串为数组
    print("****************************************")
    print("您查询的IP地址 %s 来源地是（限制50次每天）："%args)
    print("国家：%s"%(str[0]))  #访问数组里面的值
    print("省份：%s"%(str[1]))
    print("城市：%s"%(str[2]))
    print("区域：%s"%(str[3]))
    str[4] = str[4].replace('\n', '') #去掉回车符号
    print("运营商：%s"%(str[4]))
    print("数据来源<www.ipip.net免费查询接口>")
    print("****************************************")
if __name__ == "__main__":
    main(sys.argv)
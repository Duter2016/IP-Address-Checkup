#! /usr/bin/python3
#coding=utf-8
'''
Created on Jun.10 2021
@author: kelven & duter2016
'''
import sys
import requests
import urllib.request

def main(argv):

    url2 = 'http://ip-api.com/json/'   #外国网站，ipv4及ipv6
    url2cn = '?lang=zh-CN'   #ip-api中文接口
    args = sys.argv[1]
    url2 = url2 + format(args) + url2cn
    response2 = requests.get(url2)

    print("****************************************")
    strpp={}                  #定义一个字典strpp   
    strpp=response2.json()    #把英文网站json接口返回值传给字典strpp
    print("\n")               #下面就是直接从字典取值，显示。
    print("您查询的IP地址 %s 来源地是："%(strpp.get('query')))
    print("国家：%s"%(strpp.get('country')))
    print("城市：%s"%(strpp.get('city')))
    print("经纬度坐标：%s,%s"%(strpp.get('lat'),strpp.get('lon')))
    print("运营商编号：%s"%(strpp.get('as')))
    print("ISP服务商：%s"%(strpp.get('isp')))
    print("数据来源<www.ip-api.com免费查询接口>.")
    print("****************************************")
if __name__ == "__main__":
    main(sys.argv)
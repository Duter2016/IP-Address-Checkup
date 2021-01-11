#! /usr/bin/python3
#coding=utf-8
'''
Created on Jun.10 2021
@author: kelven & duter2016
利用高德地图api实现经纬度与地址的转换
'''
import sys
import requests
import json
from bs4 import BeautifulSoup

def geocode(location):
    parameters = {'location': location, 'key': '1937b7ce560bb5124088b2cc5c07687b'}
    base = 'http://restapi.amap.com/v3/geocode/regeo'
    response4 = requests.get(base, parameters)
    answer = response4.json()
    return answer

def geocodebatch(location):
    parameters = {'location': location, 'key': '1937b7ce560bb5124088b2cc5c07687b', 'batch': 'true'}
    base = 'http://restapi.amap.com/v3/geocode/regeo'
    response4 = requests.get(base, parameters)
    answer = response4.json()
    return answer

def main(argv):

    url = 'http://freeapi.ipip.net/'   #中文免费，免费版仅ipv4
    url2 = 'http://ip-api.com/json/'   #外国网站，ipv4及ipv6
    url2cn = '?lang=zh-CN'   #ip-api中文接口，ipv4及ipv6
    url3 = 'https://ip.yinghualuo.cn/api?ip='   #中文免费，ipv4及ipv6
    url4 = 'http://restapi.amap.com/v3/ip?ip='  #高德地图，ipv4
    url4key = '&key=1937b7ce560bb5124088b2cc5c07687b'
    args = sys.argv[1]
    url=url+format(args)
    url2 = url2 + format(args) + url2cn
    url3 = url3 + format(args)
    url5 = url4 + format(args) + url4key
    response = requests.get(url)
    response2 = requests.get(url2)
    response3 = requests.get(url3)
    response5 = requests.get(url5)
    ipaddr = response5.json()

    strr=response.text.replace('\"','') #去掉双引号
    strr=strr.replace('[','')            #去掉方括号
    strr=strr.replace(']','')
    strr=strr.replace(' ','')
    strr=strr.split(",")   #以逗号为分割符号，分割字符串为数组

    print("****************************************")    #ip.yinghualuo.cn输出结果
    response3.encoding="utf-8"
    print("您查询的IP地址 %s 来源地是："%args)
    print(BeautifulSoup(response3.text,features="lxml").get_text(separator=" "))
    print("数据来源<ip.yinghualuo.cn免费查询接口>")
    print("****************************************")

    print("****************************************")    #高德输出结果
    ipaddrls = {}                  #定义一个字典ipaddrls，获取经纬度   
    ipaddrls = ipaddr.get('rectangle')    #获取坐标返回值传给字典ipaddrls
    print("您查询的IP地址 %s 来源地是："%args)
    print("经纬度坐标：%s"%ipaddr.get('rectangle'))
    print("下面是用高德地图逆地理编码转换经纬度获取的精确地址（限国内地址）：")
    locationa = str(ipaddr.get('rectangle'))
    locationb = geocodebatch(locationa)
    print(locationb)
    print("数据来源<高德地图lbs.amap.com免费查询接口>")
    print("****************************************")

    print("****************************************")    #www.ipip.net输出结果
    print("您查询的IP地址 %s 来源地是（限制50次每天）："%args)
    print("国家：%s"%(strr[0]))  #访问数组里面的值
    print("省份：%s"%(strr[1]))
    print("城市：%s"%(strr[2]))
    print("区域：%s"%(strr[3]))
    strr[4] = strr[4].replace('\n', '') #去掉回车符号
    print("运营商：%s"%(strr[4]))
    print("数据来源<www.ipip.net免费查询接口>")
    print("****************************************")

    print("****************************************")    #www.ip-api.com+高德输出结果
    strpp={}                  #定义一个字典strpp   
    strpp=response2.json()    #把英文网站json接口返回值传给字典strpp
    print("您查询的IP地址 %s 来源地是："%(strpp.get('query')))
    print("国家：%s"%(strpp.get('country')))
    print("城市：%s"%(strpp.get('city')))
    print("经纬度坐标：%s,%s"%(strpp.get('lon'),strpp.get('lat')))
    print("运营商编号：%s"%(strpp.get('as')))
    print("ISP服务商：%s"%(strpp.get('isp')))
    print("数据来源<www.ip-api.com免费查询接口>.")
    print("****************************************")
    print("下面是用高德地图逆地理编码转换经纬度获取的精确地址（限国内地址）：")
    locationa = str(strpp.get('lon')) + ',' + str(strpp.get('lat'))
    locationb = geocode(locationa)
    print(locationb)
    print("****************************************")

if __name__ == "__main__":
    main(sys.argv)
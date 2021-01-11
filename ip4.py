#! /usr/bin/python3
#coding=utf-8
'''
Created on Jun.10 2021
@author: kelven & duter2016
数据来源<www.ip-api.com免费查询接口>
并利用高德地图api实现经纬度与地址的转换
'''
import sys
import requests
import json

def geocodebatch(location):
    parameters = {'location': location, 'key': '你的高德地图apiKEY', 'batch': 'true'}
    base = 'http://restapi.amap.com/v3/geocode/regeo'
    response4 = requests.get(base, parameters)
    answer = response4.json()
    return answer

def main(argv):
    url4 = 'http://restapi.amap.com/v3/ip?ip='  #高德地图，ipv4
    url4key = '&key=你的高德地图apiKEY'
    args = sys.argv[1]
    url5 = url4 + format(args) + url4key
    response5 = requests.get(url5)
    ipaddr = response5.json()

    print("****************************************")
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
if __name__ == "__main__":
    main(sys.argv)


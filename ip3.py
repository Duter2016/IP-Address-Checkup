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

    url3 = 'https://ip.yinghualuo.cn/api?ip='   #中文免费，ipv4及ipv6
    args = sys.argv[1]
    url3 = url3 + format(args)
    response3 = requests.get(url3)

    print("****************************************")
    response3.encoding="utf-8"
    print("您查询的IP地址 %s 来源地是："%args)
    print(BeautifulSoup(response3.text,features="lxml").get_text(separator=" "))
    print("数据来源<ip.yinghualuo.cn免费查询接口>")
    print("****************************************")
if __name__ == "__main__":
    main(sys.argv)
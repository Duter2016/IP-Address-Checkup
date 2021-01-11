# 使用python脚本查询ip归属地

## 一、使用方法：
终端执行命令：
```
python3 ip.py 112.1.173.185         #（1）（2）（3）(4)的综合查询，每天限制50次

python3 ip1.py 112.1.173.185        #（2）的查询，每天限制50次

python3 ip2.py 112.1.173.185        #（3）的查询，无次数限制

python3 ip3.py 112.1.173.185        #（1）的查询，无次数限制

python3 ip4.py 112.1.173.185        # 高德地图的查询，无次数限制
```

## 二、可以使用的IP归属地查询接口：

###（1）国内，免费支持ipv4及ipv6
```
curl https://ip.yinghualuo.cn/api?ip=2001:da8:bc:b376:69ef:ff24:ce6:9041
curl https://ip.zxinc.org/api.php?ip=2001:da8:bc:b376:69ef:ff24:ce6:9041
```
###（2）国内，仅免费支持ipv4，每天限制50次
```
curl https://freeapi.ipip.net/112.1.173.185
```

###（3）国外，免费支持ipv4及ipv6
```
curl http://ip-api.com/json/112.1.173.185      #英文
curl http://ip-api.com/json/218.192.3.42?lang=zh-CN       #中文
```

###（4）国内，免费支持ipv4
```
curl https://ip.cn/index.php?ip=112.1.173.185  （不使用，返回信息太复杂）
```




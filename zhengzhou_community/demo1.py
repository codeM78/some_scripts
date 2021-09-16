# -*- coding: utf-8 -*-
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/8/18 20:57
# @Software: PyCharm
import requests
import urllib
import hashlib

location = input("河南省郑州市\n")  # "河南省郑州市"
# 计算校验SN(百度API文档说明需要此步骤)
ak = "jmeAIvR7b5S4fQ8yuBdVwtKPi7vgAgsI" # 参照自己的应用
sk = "VVUVwmNqMcQSClpYrQTzh4nittjRgchZ" # 参照自己的应用
url = "http://api.map.baidu.com"
query = "/geocoder/v2/?address={0}&ak={1}&output=json".format(location, ak)
encodedStr = urllib.parse.quote(query, safe="/:=&?#+!$,;'@()*[]")
sn = hashlib.md5(urllib.parse.quote_plus(encodedStr + sk).encode()).hexdigest()

# 使用requests获取返回的json
response = requests.get("{0}{1}&sn={2}".format(url, query, sn))
data = eval(response.text)
print(data)
lat = data["result"]["location"]["lat"]
lon = data["result"]["location"]["lng"]
print("纬度: ", lat, " 经度: ", lon)

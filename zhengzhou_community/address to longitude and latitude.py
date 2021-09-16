# -*- coding: utf-8 -*-
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/8/18 23:43
# @Software: PyCharm

# 导入相关的包
import requests #HTTP请求
import time
import pandas as pd # 用于处理数据（数据分析相关的同学必须会的包）

'''地址名称to经纬度'''
'''1.数据准备'''
df = pd.read_csv(r'D:\Python works\Some scripts\zhengzhou_community\files\community_name_Zhengzhou.csv',encoding="utf-8")
# print(df["community_name"])


#利用百度地图api根据地理名称获取其经纬度
def geocodeB(address):
    """
    @ address: 名称字符串
    @ 返回值：经度，纬度
    """
    #这里的ak使用自己申请的百度接口应用
    base_url = "http://api.map.baidu.com/geocoder?address={address}&output=json&key=jmeAIvR7b5S4fQ8yuBdVwtKPi7vgAgsI".format(address=address)
    response = requests.get(base_url)
    #获取响应
    answer = response.json()
    #获取经度
    latitude = answer['result']['location']['lng']
    #获取纬度
    longitude = answer['result']['location']['lat']
    time.sleep(0.1) 

    return latitude, longitude

def list_to_df(x):
    # 列表
    longitude_latitude_list = x

    # list转dataframe
    df1 = pd.DataFrame(longitude_latitude_list, columns=['longitude', 'latitude'])

    # 保存到本地csv
    df1.to_csv("longitude_latitude_Zhengzhou.csv", index=False)

    #两张数据表合并
    df0 = pd.concat([df,df1],axis=1)    #按照列合并

    #合并后的数据表存储为本地csv
    df0.to_csv("community_longitude_latitude_Zhengzhou.csv", index=False)



if __name__ == '__main__':
    # print(geocodeB('郑州市'))  # (113.631419, 34.753439)
    # df = df.loc[0:20]   #21个数据试试水
    #一次性加载，过于频繁，老是出错
    # df = df.loc[0:2000]   #先存储2000个数据
    # df = df.loc[2001:]  # 存储剩下的数据
    df = df.copy()
    geolist = []
    for i,a in enumerate(df["community_name"]):
        # i += 2001
        # 记得加上郑州市，只有社区名字的话不是很精准
        geolist.append(geocodeB(f"郑州市{a}"))
        print(f"---第{i}条记录已经持久化---")
    # print(geolist)
    list_to_df(geolist)
    print(f"---任务已完成！---")


# #批量数据形成字典一一对应
# df = df.loc[0:10]   #11个数据试试水
# geolist = []
# for i in df["community_name"]:
#     geolist.append(i)
# store_geo_list = []
# dictvar = dict()
#
# for geo in geolist:
#     store_geo__dict = {}
#     listvar = list(geocodeB(f"郑州市{geo}"))   #这里加上郑州市，搜索更精准
#     store_geo__dict['经度'] = listvar[0]
#     store_geo__dict['纬度'] = listvar[1]
#     dictvar[geo] = store_geo__dict
# print(dictvar)



#将字典转换为列表
# df = pd.DataFrame.from_dict(dictvar,
#                             orient="index",  #按照行排列
#                             columns=['community_name','longitude and latitude']
#                            )
# df = df.reset_index().rename(columns = {'index':'id'})
# print(df)






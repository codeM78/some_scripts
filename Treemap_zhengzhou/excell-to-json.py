# codeing : utf-8
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/8/22 19:46
# @Software: PyCharm
#先导入数据
import pandas as pd
import numpy as np
import json

'''将excell表格转换为json格式'''
data = pd.read_excel('data/test.xls')
# print(data)

### 特意调整好了格式 希望大家能看的懂
### 说明：以_dict结尾的变量名用来装这一层的数据,包括两部分，区(如城市份)，数据(data),data等于_list数组；以_list结尾的变量名用来装下一级的所有数据，最后_list就是这一层的数据data
json_list = []
for city in data['city'].unique():                              #选一城市
    city_dict={}                                             	#建一个字典，用来存储  城市和该城市的数据
    city_dict['city'] = city                                 	#   城市
    city_list = []                                           	#建一个列表  用来存储 该城市的数据； 现在数据暂时为空，需要在后面添加
    city_data = data[data['city']==city]                     	#将数据降一级，只看该城市的数据

    for cistrict in city_data['cistrict'].unique():                  	#选一区
        cistrict_dict={}                                         	#建一个字典，用来存储  区和该区的数据
        cistrict_dict['cistrict'] = cistrict                             	# 区
        cistrict_list = []                                       	#建一个列表  用来存储 该区的数据； 现在数据暂时为空，需要在后面添加
        cistrict_data = city_data[city_data['cistrict']==cistrict]       	#将数据降一级，只看该区的数据

        for community in cistrict_data['community'].unique():             	#选一个社区
            community_dict = {}                                  	#建一个字典，用来存储  社区和该区的数据
            community_dict['community'] = community                      	#社区
            community_list = []                                   	#建一个列表  用来存储 该区的数据； 现在数据暂时为空，需要在后面添加
            community_data = cistrict_data[cistrict_data['community']==community]

            for city in data.columns[3:]:                      #这里建议直接用原始数据data来分割，第4列以后的是数据
                info={}											#建一个字典，用来存储  城市和该市的数据
                info['city'] = city								#城市
                info['data'] = community_data.iloc[0][city]         #此时每个community_data只有一行数据了,就可以去除数值了
                community_list.append(info)							#将info加到community_list中

            community_dict['data'] = community_list                     #community_list是community_dict的数据
            cistrict_list.append(community_dict)						#将community_dict加到cistrict_list中

        cistrict_dict['data'] = cistrict_list							#cistrict_list是cistrict_dict的数据
        city_list.append(cistrict_dict)								#将cistrict_dict加到year_list中

    city_dict['data'] = city_list								#year_list是year_dict的数据
    json_list.append(city_dict)


#保存为json文件
# json_dict = {}
# json_dict['data'] = json_list
data_dict = json.dumps(json_list, ensure_ascii=False)
with open('data/data1.json', 'w', encoding='utf-8') as f_w:
    f_w.write(data_dict)

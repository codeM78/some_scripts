# -*- codeing: utf-8 -*-
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/8/20 14:59
# @Software: PyCharm
import pandas as pd

'''为circle packing环形分级图适配数据格式'''
data = {}
# data0 = data[0]['children']
# print(data0)

#获取数据
df = pd.read_csv(r'data/district_name.csv', encoding='utf-8')
# print(df.head())

for district in df['district_name']:   #第一层级-区县
    data[f'{district}'] = {"$count": 830000}

    df_town = pd.read_csv(f'data/{district}/{district}_town_name.csv', encoding='utf-8')
    for j,town in enumerate(df_town['town_name']):  #第二层级-乡镇与街道
        v_town = 830000 // len(df_town['town_name'])    #设定每个街道的值
        data[f'{district}'][f'{town}'] = {"$count": v_town}

        df_down_c = pd.read_csv(f'data/{district}/{district}_town_community{j}_name.csv', encoding='utf-8')
        for community in df_down_c['community_name']:   #第三层级-村落与社区
            v_community = v_town // len(df_down_c['community_name'])  #设定每个社区的值
            data[f'{district}'][f'{town}'][f'{community}'] = {"$count": v_community}

print(data)




# 将数据转化为json格式
import json
jsonArr = json.dumps(data, ensure_ascii=False)  #ensure_ascii=False让中文字符正常显示
with open('files/data_demo2_test.json', 'w', encoding='utf-8') as f_j:
    f_j.write(jsonArr)


#数据集合：


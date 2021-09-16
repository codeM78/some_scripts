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
        data[f'{district}'][f'{town}'] = {"$count": 28000}

        df_down_c = pd.read_csv(f'data/{district}/{district}_town_community{j}_name.csv', encoding='utf-8')
        for community in df_down_c['community_name']:   #第三层级-村落与社区
            data[f'{district}'][f'{town}'][f'{community}'] = {"$count": 1000}

print(data)




# 将数据转化为json格式
import json
jsonArr = json.dumps(data, ensure_ascii=False)  #ensure_ascii=False让中文字符正常显示
with open('files/data_demo2.json', 'w', encoding='utf-8') as f_j:
    f_j.write(jsonArr)


#数据集合：


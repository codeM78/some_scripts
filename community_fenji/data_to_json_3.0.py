# -*- codeing: utf-8 -*-
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/8/20 14:59
# @Software: PyCharm
import pandas as pd

data = []

#获取数据
df = pd.read_csv(r'data/district_name.csv', encoding='utf-8')


for k,district in enumerate(df['district_name']):   #第一层级-区县
    district_dict = {
        "name": f"{district}",
        "children": []
    }
    # data[0]['children'].append(district_dict)
    data.append(district_dict)

    df_town = pd.read_csv(f'data/{district}/{district}_town_name.csv', encoding='utf-8')
    for j,town in enumerate(df_town['town_name']):  #第二层级-乡镇与街道
        town_dict = {

            "name": f"{town}",
            "value": 100,
            "children": []
        }
        # data[0]['children'][k]['children'].append(town_dict)
        data[k]['children'].append(town_dict)

        df_down_c = pd.read_csv(f'data/{district}/{district}_town_community{j}_name.csv', encoding='utf-8')
        for community in df_down_c['community_name']:   #第三层级-村落与社区
            community_dict = {

                "name": f"{community}",
                "value": 3
            }
            # data[0]['children'][k]['children'][j]['children'].append(community_dict)
            data[k]['children'][j]['children'].append(community_dict)

print(data)

#将数据转化为json格式
import json
jsonArr = json.dumps(data, ensure_ascii=False)  #ensure_ascii=False让中文字符正常显示
with open('files/data_demo3.json', 'w', encoding='utf-8') as f_j:
    f_j.write(jsonArr)

#数据集合：


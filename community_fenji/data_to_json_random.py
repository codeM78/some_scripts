# -*- codeing: utf-8 -*-
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/8/20 14:59
# @Software: PyCharm
import pandas as pd
import numpy as np


#需求：生成和为固定值n的m个随机数
def n_random_m(n:int,m:int):
    # 生成和为固定值n的m个随机整数

    import numpy as np
    random_num = np.random.randint(n,size=m-1)
    ratio = sum(random_num)/n
    result = random_num//ratio
    result = result.tolist()
    result.append(n-sum(result))

    return result


data = []
Zhengzhou_num = 12600600
#获取数据
df = pd.read_csv(r'data/district_name.csv', encoding='utf-8')


for k,district in enumerate(df['district_name']):   #第一层级-区县
    v_district = n_random_m(Zhengzhou_num,len(df['district_name'])) #随机设定每个区的值
    district_dict = {
        "value": v_district[k],
        "name": f"{district}",
        "path": f"郑州市/{district}",
        "children": []
    }
    data.append(district_dict)

    df_town = pd.read_csv(f'data/{district}/{district}_town_name.csv', encoding='utf-8')
    for j,town in enumerate(df_town['town_name']):  #第二层级-乡镇与街道
        # v_town = 830000 // len(df_town['town_name'])
        v_town = n_random_m(v_district[k],len(df_town['town_name'])) #随机设定每个街道的值
        town_dict = {
            "value": v_town[j],
            "name": f"{town}",
            "path": f"郑州市/{district}/{town}",
            "children": []
        }
        data[k]['children'].append(town_dict)

        df_down_c = pd.read_csv(f'data/{district}/{district}_town_community{j}_name.csv', encoding='utf-8')
        for l,community in enumerate(df_down_c['community_name']):   #第三层级-村落与社区
            # v_community = v_town // len(df_down_c['community_name'])
            #这里的v_town[j]+1保证参数m＞0，否则会出错
            v_community = n_random_m(v_town[j]+1,len(df_down_c['community_name'])) #随机设定每个社区的值

            #处理空值nan
            if np.isnan(v_community[l]):
                v_community[l] = 0.0
                community_dict = {
                    "value": v_community[l],
                    "name": f"{community}",
                    "path": f"郑州市/{district}/{town}/{community}",
                    "children": []
                }
                data[k]['children'][j]['children'].append(community_dict)
            else:
                community_dict = {
                    "value": v_community[l],
                    "name": f"{community}",
                    "path": f"郑州市/{district}/{town}/{community}",
                    "children": []
                }
                data[k]['children'][j]['children'].append(community_dict)


# print(data)

#将数据转化为json格式
import json
jsonArr = json.dumps(data, ensure_ascii=False)  #ensure_ascii=False让中文字符正常显示
with open('files/data_random.json', 'w', encoding='utf-8') as f_j:
    f_j.write(jsonArr)



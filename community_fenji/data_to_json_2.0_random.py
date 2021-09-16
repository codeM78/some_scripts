# -*- codeing: utf-8 -*-
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/8/20 14:59
# @Software: PyCharm
import numpy as np
import pandas as pd

'''为circle packing环形分级图适配数据格式'''
data = {}
# data0 = data[0]['children']
# print(data0)

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

# re = n_random_m(100,8)
# print(re)

#使用目前随机数目的话，会出现很多的0，暂时不是太好
#获取数据
df = pd.read_csv(r'data/district_name.csv', encoding='utf-8')
# print(df.head())
Zhengzhou_num = 12600600

for i,district in enumerate(df['district_name']):   #第一层级-区县
    v_district = n_random_m(Zhengzhou_num,len(df['district_name'])) #随机设定每个区的值
    data[f'{district}'] = {"$count": v_district[i]}

    df_town = pd.read_csv(f'data/{district}/{district}_town_name.csv', encoding='utf-8')
    for j,town in enumerate(df_town['town_name']):  #第二层级-乡镇与街道
        # v_town = 830000 // len(df_town['town_name'])    #设定每个街道的值
        v_town = n_random_m(v_district[i],len(df_town['town_name'])) #随机设定每个街道的值
        data[f'{district}'][f'{town}'] = {"$count": v_town[j]}

        df_down_c = pd.read_csv(f'data/{district}/{district}_town_community{j}_name.csv', encoding='utf-8')
        for l,community in enumerate(df_down_c['community_name']):   #第三层级-村落与社区
            # v_community = v_town // len(df_down_c['community_name'])  #设定每个社区的值
            #这里的v_town[j]+1保证参数m＞0，否则会出错
            v_community = n_random_m(v_town[j]+1,len(df_down_c['community_name'])) #随机设定每个社区的值

            #处理缺失值nan
            if np.isnan(v_community[l]):
                v_community[l] = 0.0
                data[f'{district}'][f'{town}'][f'{community}'] = {"$count": v_community[l]}
            else:
                data[f'{district}'][f'{town}'][f'{community}'] = {"$count": v_community[l]}


# print(data)




# 将数据转化为json格式
import json
jsonArr = json.dumps(data, ensure_ascii=False)  #ensure_ascii=False让中文字符正常显示
with open('files/data_demo2_random.json', 'w', encoding='utf-8') as f_j:
    f_j.write(jsonArr)


#数据集合：


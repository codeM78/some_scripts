# -*- coding: utf-8 -*-
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/8/19 8:25
# @Software: PyCharm

import pandas as pd

'''读取数据'''
# df1 = pd.read_csv(r"D:\Python works\Some scripts\community_name_Zhengzhou.csv")
# df2 = pd.read_csv(r"D:\Python works\Some scripts\longitude_latitude_Zhengzhou.csv")
# #查看数据
# # print(df1.index)
# # print(df2)
#
# df = pd.concat([df1,df2], axis=1)    #按照列合并,此时列的名称不能有重复项。同理，axis=0为按照行合并，索引不能有重复
# # print(df)
# #持久化到本地
# # df.to_csv("All_community_longitude_latitude_Zhengzhou.csv", index=False, encoding='utf-8')
# df.to_excel("All_community_longitude_latitude_Zhengzhou.xlsx", index=False, encoding='utf-8')

df = pd.read_excel(r"D:\Python works\Some scripts\zhengzhou_community\All_community_longitude_latitude_Zhengzhou.xlsx")
# print(df.head())

#筛选表格中错误地理信息
df_1 = df[df['latitude']>35]
df_2 = df[df['latitude']<34]
df_F = pd.concat([df_1,df_2],axis=0)
# print(df_F)
# df_F.to_excel("F_community_longitude_latitude_Zhengzhou.xlsx", index=False, encoding='utf-8')

#全表格减去错误信息表格, ~表示取反，在错误信息中的数据取反（就是全数据中不在错误数据中的正确数据）
df_T = df[~df["community_name"].isin(df_F["community_name"])]
df_T.to_excel("T_community_longitude_latitude_Zhengzhou.xlsx", index=False, encoding='utf-8')


# coding=utf-8
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/9/14 20:17
# @Software: PyCharm


import pandas as pd

'''将这两张表，按照国家缩写码，合并一下，合成一张大表。'''
def heBing():
    # Todo: Add your code here
    df1 = pd.read_csv('../data/data.csv')
    df2 = pd.read_csv('../data/data2.csv')
    print(df1.head())
    print(df2.head())
    # 表连接，类似于数据库表的内连接，不匹配的值直接不予保留
    df = pd.merge(df1,df2,left_on='国家码',right_on='国际域名缩写')
    # print(df)
    df.to_csv('../data/合并表_无索引.csv', encoding='utf-8', index=False)

def dataProcess():
    # 运营商名称(MCC)扩展一下。如MoviStar（21402）。
    df = pd.read_csv('../data/合并表_无索引.csv')
    # print(df.head())
    #列合并  如果列值为非字符串类型，记得转换为字符串类型，才能拼接
    df['运营商_MCCMNC'] = df['运营商']+'('+df['MCC3_MNC2'].astype(str)+')'
    print(df.head())
    df.to_csv('../data/新合并表.csv', encoding='utf-8', index=False)

if __name__ == '__main__':
    pass
    # heBing()
    dataProcess()
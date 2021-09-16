# coding=utf-8
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/9/8 20:58
# @Software: PyCharm

import pickle
# pkl_file = open('./output/test.pkl', 'rb')
# data1 = pickle.load(pkl_file)

# with open('./output/test.pkl', 'rb') as pkl_file:
#     data1 = pickle.load(pkl_file)
#
# print(len(data1)) #1412个样本


'''查看数据的活还是jupyter notebook好用'''
# with open('./output/macbert_fold0.pkl', 'rb') as pkl_file:
#     data_macbert_fold0 = pickle.load(pkl_file)
#
# print(data_macbert_fold0)
# #PKL中存储了输出结果的相关信息序号，标签和概率值。[index,outputs[0]['label'],outputs[0]['score']]

import pandas as pd
df = pd.read_csv('./data/input.csv')

y = 1 * (df.cand_pty_affiliation == "REP")
x = df.drop(['cand_pty_affiliation'],axis=1)
x = pd.get_dummies(x,sparse=True)
# x.drop(x.columns[x.std()==0],axis=1,inplace=True) #报错
# print(x)
# print(x.columns[x.std()==0])
# print(x.columns[x.std()==0])  #默认按照列求方差
# print(x.std())
for i in [x.std()==0]:
    print(i)


# def get_train_test():   # 数据处理
#
#     y = 1 * (df.cand_pty_affiliation == "REP")
#     x = df.drop(['cand_pty_affiliation'],axis=1)
#     x = pd.get_dummies(x,sparse=True)
#     x.drop(x.columns[x.std()==0],axis=1,inplace=True) #报错
#     # return train_test_split(x,y,test_size=0.95,random_state=SEED)

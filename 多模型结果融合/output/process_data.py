import io
import os
import string
import math
import pandas as pd
import regex as re
import subprocess
import pickle
import re
import csv
import random
import pandas as pd

"""
     非标准化疾病诉求的简单分诊挑战赛  数据预处理
"""
data_path = '/media/shared/huangruiyang/data/fenzhen'

def StatTrainDataSets():
    '''用于统计训练数据集的数据分布等情况'''
    train_file = os.path.join(data_path, 'dataset/train.xlsx')
    print('第1步，进行数据集的处理')
    df = pd.read_excel(train_file)
    # 对空值
    df = df.fillna('')
    maxLen = -99
    labels = [0]*10
    for index,row in df.iterrows():
        # diseaseName = str(row[2])
        # conditionDesc = str(row[3])
        # title = str(row[4])
        diseaseName = row[2]
        conditionDesc = row[3]
        title = row[4]
        hopeHelp = row[5]
        lable = row[6]
        cur_len = len(diseaseName)+len(title)+len(conditionDesc)
        if(cur_len>maxLen):
            maxLen = cur_len
            print(diseaseName,title,conditionDesc,'   | ', hopeHelp)
        labels[lable]+=1
    # print(df.columns)
    # print(df.head(20))
    print(labels)
    print(maxLen)
    # 类别统计：总共有10类，最长为254，其中第9类的数量有点过少。
    # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    # [842, 818, 824, 806, 1086, 947, 516, 843, 888, 274]
    # 254

def CreateTrainData_Fold5(output_dir):
    '''训练数据集的划分：5折数据'''
    '''用于统计训练数据集的数据分布等情况'''
    train_file = os.path.join(data_path, 'dataset/train.xlsx')
    print('第1步，进行数据集的读取...')
    df = pd.read_excel(train_file)
    # 对空值
    df = df.fillna('')
    total_data = {}
    maxLen = -99
    labels = [0]*10
    print('第2步，分类别进行数据整理...')
    for index,row in df.iterrows():
        # diseaseName = str(row[2])
        # conditionDesc = str(row[3])
        # title = str(row[4])
        diseaseName = row[2]
        conditionDesc = row[3]
        title = row[4]
        label = row[6]
        # 创建每个标签的数组
        if(label not in total_data):
            total_data[label] = []
        if(len(title)<1):
            total_data[label].append([diseaseName+'。'+conditionDesc,label])
        else:
            total_data[label].append([title+'。'+diseaseName+'。'+conditionDesc,label])

    #     split_every = int(len(wav_list)*ratio)
    #     # 创建十折的数据
    #     for i in range(batch):
    #         # if(i==9):
    #         land_wavfiles[lang_dir].append(wav_list[i*split_every:(i+1)*split_every])
    #     # 对最后一个处理，将剩下的统一赋值给最后一个值 
    #     land_wavfiles[lang_dir][-1].extend(wav_list[10*split_every:])
    # print('第3步，创建分折的数据...')

    total_list = [0,1,2,3,4]
    batch = 5
    ratio= 0.2
    # 构造5折的数据集
    for fold_id in range(batch):
        print('fold :', fold_id)
        train_folds = total_list.copy()
        val_folds = batch-1-fold_id
        train_folds.remove(batch-1-fold_id)
        print(val_folds, train_folds)
        # 数据集
        train_dataset=[]
        val_dataset =[]
        for key,item in total_data.items():
            print(key,len(item))
            split_every = int(len(item)*ratio)
            val_list = []
            # 如果不是最后一折，只计算所有的值
            if(val_folds<4):
                val_list= item[val_folds*split_every:(val_folds+1)*split_every]
            else:
                 val_list= item[val_folds*split_every:]
            # list(set(item) - set(val_list))
            train_list = [x for x in item if x not in val_list]
            train_dataset.extend(train_list)
            val_dataset.extend(val_list)
        fold_key = '/fold%d'% fold_id
        # 创建文件夹
        if(not os.path.exists(output_dir + fold_key)):
            os.makedirs(output_dir +fold_key)
        # 保存每一折的数据信息
        create_fold_csv(dataset=train_dataset, output_filename=output_dir + '%s/train.csv' % fold_key)
        create_fold_csv(dataset=val_dataset, output_filename=output_dir + '%s/dev.csv' % fold_key)
        create_fold_csv(dataset=val_dataset, output_filename=output_dir + '%s/test.csv' % fold_key)
    pass


def create_fold_csv(dataset,output_filename):
    """
    """

    # Starting index
    idx = 0
    # CSV column titles
    csv_header = ["sentence", "label"]

    # Add titles to the list at indexx 0
    dataset.insert(0, csv_header)

    # Writing the csv lines
    with open(output_filename, mode="w", encoding="utf-8") as csv_f:
        csv_writer = csv.writer(
            csv_f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        for line in dataset:
            csv_writer.writerow(line)

def StatTestDataSets():
    '''用于统计训练数据集的数据分布等情况'''
    train_file = os.path.join(data_path, 'dataset/test.xlsx')
    print('第1步，进行数据集的处理')
    df = pd.read_excel(train_file)
    # 对空值
    df = df.fillna('')
    maxLen = -99
    labels = [0]*10
    test_data = []
    for index,row in df.iterrows():
        # diseaseName = str(row[2])
        # conditionDesc = str(row[3])
        # title = str(row[4])
        diseaseName = row[2]
        conditionDesc = row[3]
        title = row[4]
        hopeHelp = row[5]
        label = -1
        cur_len = len(diseaseName)+len(title)+len(conditionDesc)
        if(cur_len>maxLen):
            maxLen = cur_len
            print(diseaseName,title,conditionDesc,'   | ', hopeHelp)
        if(len(title)<1):
            test_data.append([diseaseName+'。'+conditionDesc,label])
        else:
            test_data.append([title+'。'+diseaseName+'。'+conditionDesc,label])
        # labels[lable]+=1
    # print(df.columns)
    # print(df.head(20))
    pickle.dump(test_data,open(data_path+'/dataset/test.pkl','wb'))
    create_fold_csv(dataset=test_data, output_filename=data_path + '/0828/test.csv')

if __name__ == "__main__":
    #  用于统计训练数据集的数据分布等情况 
    # StatTrainDataSets()
    # output_dir = data_path+'/0828'
    # CreateTrainData_Fold5(output_dir)

    StatTestDataSets()
    print('work done!')

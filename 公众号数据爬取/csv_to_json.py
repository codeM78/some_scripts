# coding=utf-8
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/9/14 21:33
# @Software: PyCharm

import pandas as pd

def dataProcess():


    '''为树状图适配数据格式'''
    '''
    需求：做成树状图，按国家来操作，国家到运营商。MoviStar（21402）。
    看起来只需要两级，国家或地区->运营商_MCCMNC。使用新合并表（只需要两列--国家或地区，运营商_MCCMNC）
    '''

    data = {'name':'国家地区—运营商','children':[]}

    #获取数据
    df = pd.read_csv(r'data/新合并表.csv', encoding='utf-8')
    # print(df['国家或地区'].unique()) #去除重复值
    # print(df['运营商_MCCMNC'][0:4])

    for i,country in enumerate(df['国家或地区'].unique()):   #第一层级-国家或地区
        country_dict = {
            "name": f"{country}",
            "children": []
        }
        data['children'].append(country_dict)

        for j,country_ in enumerate(df['国家或地区']):
            # print(country_)
            if country_ == country:
                # print(df['运营商_MCCMNC'][k])
                #Operators运营商字典
                operators_dict = {
                            "name": f"{df['运营商_MCCMNC'][j]}",
                            # "children": []
                            # "value": 100
                        }
                data['children'][i]['children'].append(operators_dict)

    return data
    # print(data)


def csv2json():
    # 将数据转化为json格式
    import json
    jsonArr = json.dumps(dataProcess(), ensure_ascii=False)  #ensure_ascii=False让中文字符正常显示
    with open('data/test_novalue.json', 'w', encoding='utf-8') as f_j:
        f_j.write(jsonArr)
    print('转换完成')


if __name__ =="__main__":
    # csv2json()
    # dataProcess()

    # #获取提示框数据
    # df = pd.read_csv(r'data/新合并表.csv', encoding='utf-8')
    # df['国家或地区_运营商_MCCMNC'] = df['国家或地区']+'.'+df['运营商_MCCMNC'].astype(str)
    # # print(df.head())
    # df.to_csv(r'data/新合并表2.csv', index=False)
    # lst = [i for i in df['国家或地区_运营商_MCCMNC']]
    # print(lst)



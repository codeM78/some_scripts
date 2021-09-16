# coding=utf-8
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/9/14 9:44
# @Software: PyCharm
import re

import pandas as pd
from bs4 import BeautifulSoup
def getData():
    # Todo: Add your code here
    with open('htmldome.html', 'rb') as f:
        html = f.read().decode('utf-8')
    bs = BeautifulSoup(html,'html.parser')  #形成了树形结构
    # print(bs.table)
    data = bs.find_all('table')
    html_table2 = str(data[2])
    bs2 = BeautifulSoup(html_table2,'html.parser')  #形成了树形结构


    # t_list = bs2.select('td > p')  #有的空值没有p标签
    # print(len(t_list)) #956
    # 成功定位表格元素
    t_list = bs2.select('td') #text中有空值''
    # print(len(t_list)) #965 果然是差了不少
    table2_list=[]
    for index,item in enumerate(t_list):
        #去除数据中的\n
        data = re.sub(r'[\n]','',item.text)
        table2_list.append(data)
    # print(table2_list)
    # print(len(table2_list))

    #将每5个一组成为一个小列表
    data_table2 = []
    for index in range(0,967,5):
        # print(index)
        data1 = table2_list[index:index+5]
        data_table2.append(data1)

    return data_table2

def list_to_df():
    # 列表
    data = getData()[1:-1]
    # print(data)

    names = ['Countries and Regions', '国家或地区', '国际域名缩写', '电话代码', '时差']
    df = pd.DataFrame(data,columns=names)

    # 字典
    # dict = {
    #     'MCC3':data[0],
    #     '国家外文名':data[1],
    #     '国家码':data[2],
    #     '国家中文名':data[3]
    # }
    #
    # #将字典转换成为数据框
    # df = pd.DataFrame(dict)


    # 保存到本地csv
    df.to_csv("data_test.csv", encoding='utf-8', index=False)
    print('保存完成！')



if __name__ == '__main__':
    pass
    # getData()
    list_to_df()

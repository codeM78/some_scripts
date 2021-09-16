# codeing : utf-8
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/8/22 22:29
# @Software: PyCharm
#先导入数据
import pandas as pd
import numpy as np
import json

# data = pd.read_excel('files/T_community_longitude_latitude_Zhengzhou.xlsx',sheet_name='整理后的数据')

import xlrd,json
def read_xlsx_file(filename):
    # 打开Excel文件
    data = xlrd.open_workbook(filename)
    # 读取第一个工作表
    table = data.sheets()[0]
    # 统计行数
    rows = table.nrows
    data = []   # 存放数据
    for i in range(1, rows):
        values = table.row_values(i)
        data.append(
            (
                {
                    "code":str(int(values[0])),
                    "name":values[1],
                }
            )
        )
    return data

if __name__ == '__main__':
    d1 = read_xlsx_file("files/T_community_longitude_latitude_Zhengzhou.xlsx")
    # 字典中的数据都是单引号，但是标准的json需要双引号
    js = json.dumps(d1,sort_keys=True,ensure_ascii=False,indent=4, separators=(',', ':'))
    print(js)
    # 前面的数据只是数组，加上外面的json格式大括号
    js = "{"+js+"}"
    # 可读可写，如果不存在则创建，如果有内容则覆盖
    jsFile = open("./text3.json", "w+", encoding='utf-8')
    jsFile.write(js)
    jsFile.close()

# codeing : utf-8
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/8/23 23:06
# @Software: PyCharm

import pandas as pd
import numpy as np

#把现有的社区数据更改为需要的数据
#目前两大问题，1.需要对每个社区赋值（可以是任意值，但是有真实意义的值最好，比如当地人口或者GDP）
#2.如何对已获取的社区进行区划分和县市划分
data1 = [
        {
            "value": 12600574,
            "name": "郑州市",
            "path": "郑州市",
            "children": [
                {
                    "value":1172237 ,
                    "name": "新郑市",
                    "path": "郑州市/新郑市",
                    "children": [
                        {
                            "value":300000,
                            "name": "龙湖镇",
                            "path": "郑州市/新郑市/龙湖镇"
                        },
                        {
                            "value":200000,
                            "name": "新建路街道",
                            "path": "郑州市/新郑市/新建路街道"
                        },
                        {
                            "value":250000 ,
                            "name": "新华路街道",
                            "path": "郑州市/新郑市/新华路街道"
                        },
                        {
                            "value":200000 ,
                            "name": "孟庄镇",
                            "path": "郑州市/新郑市/孟庄镇"
                        }
                    ]
                },
                {
                    "value": 1617541,
                    "name": "金水区",
                    "path": "郑州市/金水区",
                    "children": [
                        {
                            "value":500000 ,
                            "name": "文化路街道办事处",
                            "path": "郑州市/金水区/文化路街道办事处"
                        },
                        {
                            "value":300000 ,
                            "name": "南阳新村街道办事处",
                            "path": "郑州市/金水区/南阳新村街道办事处"
                        },
                        {
                            "value":30000 ,
                            "name": "经八路街道办事处",
                            "path": "郑州市/金水区/经八路街道办事处"
                        },
                        {
                            "value":240000 ,
                            "name": "大石桥街道办事处",
                            "path": "郑州市/金水区/大石桥街道办事处"
                        },
                        {
                            "value":150000 ,
                            "name": "人民路街道办事处",
                            "path": "郑州市/金水区/人民路街道办事处"
                        }
                    ]
                },
                {
                    "value":1061263 ,
                    "name": "二七区",
                    "path": "郑州市/二七区",
                    "children": [
                        {
                            "value":800000 ,
                            "name": "大学路街道办事处",
                            "path": "郑州市/二七区/大学路街道办事处"
                        }
                    ]
                },
                {
                    "value":962642 ,
                    "name": "中原区",
                    "path": "郑州市/中原区",
                    "children": [
                        ]
                },
                {
                    "value":819439 ,
                    "name": "管城回族区",
                    "path": "郑州市/管城回族区",
                    "children": [
                    ]
                },
                {
                    "value":197399 ,
                    "name": "上街区",
                    "path": "郑州市/上街区",
                    "children": [
                    ]
                },
                {
                    "value":555002 ,
                    "name": "惠济区",
                    "path": "郑州市/惠济区",
                    "children": [
                    ]
                },
                {
                    "value":328812 ,
                    "name": "经开区",
                    "path": "郑州市/经开区",
                    "children": [
                    ]
                },
                {
                    "value":546226 ,
                    "name": "高新区",
                    "path": "郑州市/高新区",
                    "children": [
                    ]
                },
                {
                    "value":621382 ,
                    "name": "航空港区",
                    "path": "郑州市/航空港区",
                    "children": [
                    ]
                },
                {
                    "value":945234 ,
                    "name": "郑东新区",
                    "path": "郑州市/郑东新区",
                    "children": [
                    ]
                },
                {
                    "value":702657 ,
                    "name": "中牟县",
                    "path": "郑州市/中牟县",
                    "children": [
                    ]
                },
                {
                    "value":785242 ,
                    "name": "巩义市",
                    "path": "郑州市/巩义市",
                    "children": [
                    ]
                },
                {
                    "value":730135 ,
                    "name": "荥阳市",
                    "path": "郑州市/荥阳市",
                    "children": [
                    ]
                },
                {
                    "value":826031 ,
                    "name": "新密市",
                    "path": "郑州市/新密市",
                    "children": [
                    ]
                },
                {
                    "value":729332 ,
                    "name": "登封市",
                    "path": "郑州市/登封市",
                    "children": [
                    ]
                }

            ]
        }
    ]
# print(data1[0])
for k,v in data1[0]['children'][0].items():
    print(f'键为：{k}')
    print(f'值为：{v}')

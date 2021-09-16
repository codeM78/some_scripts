# codeing : utf-8
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/8/22 22:47
# @Software: PyCharm
import json

data = [{'城市':'郑州市',
         'data':[{'区':'金水区',
                  'data':[{'社区':'郑大工学院社区',
                           }]}]}]
data_json = json.dumps(data)
print(data_json)



data = [{'城市':'郑州市',
         'data':[{'区':'金水区',
                  'data':[{'社区':'郑大工学院社区',
                            }]}]}]

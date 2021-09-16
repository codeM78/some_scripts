# coding=utf-8
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/9/13 23:17
# @Software: PyCharm


import time
import numpy as np
import pandas as pd
import re   #正则表达式用于匹配字符串
from selenium.webdriver import Chrome,ChromeOptions


def get_data():
    option = ChromeOptions()
    option.add_argument("--headless")  # 无头模式，隐藏游览器
    option.add_argument("--no--sandbox")  # 部署于Linux服务器时禁用沙盘需要
    browser = Chrome(options=option
                     ,executable_path="../zhengzhou_community/chromedriver.exe"
                     )
    try:
        #获取公众号数据
        url1 = "https://mp.weixin.qq.com/s/0t77LRkRqi_xupo0KY599g"
        browser.get(url1)
        #获取数据  //*[@id="js_content"]/table[2]/tbody/tr[2]/td[1]/p
        c_MCC = browser.find_elements_by_xpath('//*[@id="js_content"]/table[2]/tbody/tr/td[1]/p')
        #国家外文名
        c_foreign_name = browser.find_elements_by_xpath('//*[@id="js_content"]/table[2]/tbody/tr/td[2]/p')
        #国家外文名简拼
        c_foreign_name_simple = browser.find_elements_by_xpath('//*[@id="js_content"]/table[2]/tbody/tr/td[3]/p')

        #国家中文名 //*[@id="js_content"]/table[2]/tbody/tr[1]/td[4]/p
        Country_name = []
        for i in range(1,173):
            # //*[@id="js_content"]/table[2]/tbody/tr[1]/td[4]/p
            c0_Country_code = browser.find_elements_by_xpath(f'//*[@id="js_content"]/table[2]/tbody/tr[{i}]/td[4]/p')
            # 国家码  有''，需要处理
            try:
                if c0_Country_code[0].text == '':
                    Country_name.append(0)
                else:
                    Country_name.append(c0_Country_code[0].text)
            except:
                # print('这里有错误')
                Country_name.append(0)




        # MCC(3位)
        MCC  = [i.text for i in c_MCC]  # 列表生成式，获取标签内容
        # 国家外文名
        Foreign_name = [i.text for i in c_foreign_name]
        # 国家外文名简拼
        Foreign_name_simple = [i.text for i in c_foreign_name_simple]


        # print(MCC)
        # print(len(MCC)) #172
        # print(Foreign_name)
        # print(len(Foreign_name)) #172
        # print(Foreign_name_simple)
        # print(len(Foreign_name_simple)) #172

    except Exception as e:
        print(e)

    finally:
        browser.close()

    return MCC, Foreign_name, Foreign_name_simple, Country_name



def list_to_df():
    # 列表
    data = list(get_data())
    # print(data)
    dict = {
        'MCC3':data[0],
        '国家外文名':data[1],
        '国家码':data[2],
        '国家中文名':data[3]
    }

    #将字典转换成为数据框
    df = pd.DataFrame(dict)
    # 保存到本地csv
    df.to_csv("data1.csv", encoding='utf-8', index=False)
    print('保存完成！')




if __name__ == "__main__":
    list_to_df()
    # get_data()








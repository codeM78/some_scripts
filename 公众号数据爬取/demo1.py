# coding=utf-8
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/9/13 21:29
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
        #获取数据  //*[@id="js_content"]/table[1]/tbody/tr[2]/td[1]/p
        c_MCC_MNC = browser.find_elements_by_xpath('//*[@id="js_content"]/table[1]/tbody/tr/td[1]/p')
        #运营商数据  //*[@id="js_content"]/table[1]/tbody/tr[2]/td[2]/p
        c_Operators = browser.find_elements_by_xpath('//*[@id="js_content"]/table[1]/tbody/tr/td[2]/p')
        #国家码（GR） //*[@id="js_content"]/table[1]/tbody/tr[459]/td[3]
        Country_code = []
        for i in range(1,500):
            # //*[@id="js_content"]/table[1]/tbody/tr[499]/td[3]
            c0_Country_code = browser.find_elements_by_xpath(f'//*[@id="js_content"]/table[1]/tbody/tr[{i}]/td[3]/p')
            # 国家码  有''，需要处理
            try:
                if c0_Country_code[0].text == '':
                    Country_code.append(0)
                else:
                    Country_code.append(c0_Country_code[0].text)
            except:
                # print('这里有错误')
                Country_code.append(0)




        # MCC(3位)+MNC(2位)--5位数
        MCC_MNC  = [i.text for i in c_MCC_MNC]  # 列表生成式，获取标签内容
        # 运营商数据
        Operators = [i.text for i in c_Operators]


        # # print(MCC_MNC)
        # print(len(MCC_MNC)) #499
        # # print(Operators)
        # print(len(Operators)) #499
        # print('--------------------------美丽的分界线------------------------')
        # # print(Country_code)
        # print(len(Country_code))  #处理完''也是499
    except Exception as e:
        print(e)

    finally:
        browser.close()

    return MCC_MNC, Operators, Country_code



def list_to_df():
    # 列表
    data = list(get_data())
    dict = {
        'MCC3_MNC2':data[0],
        '运营商':data[1],
        '国家码':data[2]
    }

    #将字典转换成为数据框
    df = pd.DataFrame(dict)
    # 保存到本地csv
    df.to_csv("data.csv", encoding='utf-8', index=False)
    print('保存完成！')




if __name__ == "__main__":
    list_to_df()
    # get_data()







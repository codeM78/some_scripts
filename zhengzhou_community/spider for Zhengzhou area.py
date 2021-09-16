# -*- coding: utf-8 -*-
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/8/18 20:48
# @Software: PyCharm

import time
import pandas as pd
import re   #正则表达式用于匹配字符串
from selenium.webdriver import Chrome,ChromeOptions


def get_Zhengzhou():
    option = ChromeOptions()
    option.add_argument("--headless")  # 无头模式，隐藏游览器
    option.add_argument("--no--sandbox")  # 部署于Linux服务器时禁用沙盘需要
    browser = Chrome(options=option
                     # ,executable_path="chromedriver-dev.exe"
                     )

    #河南省郑州市小区名称网址
    url1 = "http://app.gjzwfw.gov.cn/jmopen/webapp/html5/unZip/18a7717c7699426dbf8b7d8b57fdccc4/hnzzsjdsqxxcxpc/index.html"  # 试试微博热搜
    browser.get(url1)
    text0 = []
    for i in range(792):
        i += 1
        print(f"------已经加载完成第{i}页社区名称------")
        #获取小区名称
        c = browser.find_elements_by_xpath('//*[@id="resultshow"]/div/ul/li[2]')
        c_ = [i.text for i in c]  # 列表生成式，获取标签内容
        text = [re.findall(r"街道社区名称：(.+)",i) for i in c_]
        #巧妙的去掉括号，实现降维
        text = sum(text,[])
        for i in text:
            text0.append(i)


        # 点击下一页按钮
        # //*[@id="nextPage"]点击下一页的按钮
        btn = browser.find_element_by_xpath('//*[@id="nextPage"]')
        btn.click()
        time.sleep(1.6)
    #关闭网页
    browser.close()
    return text0


def list_to_df():
    # 列表
    community_name_list = get_Zhengzhou()

    # list转dataframe
    df = pd.DataFrame(community_name_list, columns=['community_name'])

    # 保存到本地csv
    df.to_csv("community_name_Zhengzhou.csv", index=False)




if __name__ == "__main__":
    list_to_df()






# codeing : utf-8
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/8/24 22:10
# @Software: PyCharm

import time
import pandas as pd
import re   #正则表达式用于匹配字符串
from selenium.webdriver import Chrome,ChromeOptions


#获取区
def get_Zhengzhou():
    option = ChromeOptions()
    option.add_argument("--headless")  # 无头模式，隐藏游览器
    option.add_argument("--no--sandbox")  # 部署于Linux服务器时禁用沙盘需要
    browser = Chrome(options=option
                     ,executable_path="D:\Python works\Some scripts\zhengzhou_community\chromedriver.exe"
                     )

    #河南省郑州市小区名称网址
    # url1 = "http://app.gjzwfw.gov.cn/jmopen/webapp/html5/unZip/18a7717c7699426dbf8b7d8b57fdccc4/hnzzsjdsqxxcxpc/index.html"
    url1 = "http://www.syx7.com/Citydm.asp?Field=AreaCode&dm=4101&keyword=%BA%D3%C4%CF%CA%A1%D6%A3%D6%DD%CA%D0"
    browser.get(url1)
    data = []
    id = [410102,410103,410104,410105,410106,410108,410122,410181,410182,410183,410184,410185]
    # 和邮政编码有关  还是先将数据汇总成数据表
    for i in id:
        #获取区和县市名称
        c = browser.find_element_by_xpath(r'//*[@id="{}"]/a'.format(i))
        data.append(c.text)



    # print(data)
        # c_ = [i.text for i in c]  # 列表生成式，获取标签内容

    # for i in range(792):
    #     i += 1
    #     print(f"------已经加载完成第{i}页社区名称------")
    #     #获取小区名称
    #     c = browser.find_elements_by_xpath('//*[@id="resultshow"]/div/ul/li[2]')
    #     c_ = [i.text for i in c]  # 列表生成式，获取标签内容
    #     text = [re.findall(r"街道社区名称：(.+)",i) for i in c_]
    #     #巧妙的去掉括号，实现降维
    #     text = sum(text,[])
    #     for i in text:
    #         text0.append(i)
    #
    #
    #     # 点击下一页按钮
    #     # //*[@id="nextPage"]点击下一页的按钮
    #     btn = browser.find_element_by_xpath('//*[@id="nextPage"]')
    #     btn.click()
    #     time.sleep(1.6)
    #关闭网页
    browser.close()
    return data


def list_to_df():
    # 列表
    community_name_list = get_Zhengzhou()

    # list转dataframe
    df = pd.DataFrame(community_name_list, columns=['district_name'])

    # 保存到本地csv
    df.to_csv("../data/district_name.csv", index=False)




if __name__ == "__main__":
    # list_to_df()
    get_Zhengzhou()







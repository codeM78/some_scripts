# codeing : utf-8
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/8/24 23:50
# @Software: PyCharm


import time
import pandas as pd
import re   #正则表达式用于匹配字符串
from selenium.webdriver import Chrome,ChromeOptions

#金水区街道--获取街道
def get_Zhengzhou():
    option = ChromeOptions()
    option.add_argument("--headless")  # 无头模式，隐藏游览器
    option.add_argument("--no--sandbox")  # 部署于Linux服务器时禁用沙盘需要
    browser = Chrome(options=option
                     ,executable_path="D:\Python works\Some scripts\zhengzhou_community\chromedriver.exe"
                     )

    #中原区 看来是不能大规模成批得获取了，只能单独获取页面了。
    # urlid = [410102,410103,410104,410105,410106,410108,410122,410181,410182,410183,410184,410185]
    id = 410105
    url1 = f"http://www.syx7.com/Citydm.asp?Field=AreaCode&dm={id}&keyword=%BA%D3%C4%CF%CA%A1%D6%A3%D6%DD%CA%D0%D0%C2%D6%A3%CA%D0"
    browser.get(url1)
    data = []
    # 和邮政编码有关  还是先将数据汇总成数据表 //*[@id="410102001000"]/a
    for i in range(1,20):
        #获取区和县市名称
        if i < 10:
            c = browser.find_element_by_xpath(f'//*[@id="{id}00{i}000"]/a')
            data.append(c.text)

        else:
            c = browser.find_element_by_xpath(f'//*[@id="{id}0{i}000"]/a')
            data.append(c.text)

    print(data)
    browser.close()
    return data


def list_to_df():
    name = '金水区'
    name1 = 'town'
    # 列表
    community_name_list = get_Zhengzhou()

    # list转dataframe
    df = pd.DataFrame(community_name_list, columns=[f'{name1}_name'])   #街道

    # 保存到本地csv
    df.to_csv(f"../data/{name}/{name}_{name1}_name.csv", index=False)




if __name__ == "__main__":
    list_to_df()
    # get_Zhengzhou()









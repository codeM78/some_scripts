# codeing : utf-8
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/8/25 11:22
# @Software: PyCharm

import pandas as pd
from selenium.webdriver import Chrome,ChromeOptions


#获取社区
def get_Zhengzhou():
    option = ChromeOptions()
    option.add_argument("--headless")  # 无头模式，隐藏游览器
    option.add_argument("--no--sandbox")  # 部署于Linux服务器时禁用沙盘需要
    browser = Chrome(options=option
                     ,executable_path="D:\Python works\Some scripts\zhengzhou_community\chromedriver.exe"
                     )

    # 看来是不能大规模成批得获取了，只能单独获取页面了。
    # urlid = [410102,410103,410104,410105,410106,410108,410122,410181,410182,410183,410184,410185]
    ids = 410184   #新郑市
    data = []
    kw = '&keyword=%BA%D3%C4%CF%CA%A1%D6%A3%D6%DD%CA%D0%D0%C2%D6%A3%CA%D0'
    #冠城回族区列表
    id_list = [*range(1,4)]
    id_list.append(101)
    id_list.append(102)
    id_list.append(103)
    id_list.append(104)
    id_list.append(105)
    id_list.append(106)
    id_list.append(107)
    id_list.append(108)
    id_list.append(109)
    id_list.append(200)
    id_list.append(202)


    # print(id_list)
    for id in id_list:
        if id < 10:
            url1 = f"http://www.syx7.com/Citydm.asp?Field=AreaCode&dm={ids}00{id}{kw}"
            browser.get(url1)
            num = browser.find_element_by_xpath(f'/html/body/div[1]/b')
            num = int(num.text) + 3
            data1=[]
            for i in range(4,num):
                #获取林山寨街道办事处下得社区名称
                c = browser.find_element_by_xpath(f'/html/body/table[3]/tbody/tr[{i}]/td[1]/a')
                data1.append(c.text)
            data.append(data1)

        else :
            url1 = f"http://www.syx7.com/Citydm.asp?Field=AreaCode&dm={ids}{id}{kw}"
            browser.get(url1)
            num = browser.find_element_by_xpath(f'/html/body/div[1]/b')
            num = int(num.text) + 3
            data0=[]
            for i in range(4,num):
                #获取林山寨街道办事处下得社区名称
                c = browser.find_element_by_xpath(f'/html/body/table[3]/tbody/tr[{i}]/td[1]/a')
                data0.append(c.text)
            data.append(data0)



    print(data)
    print(len(data))
    browser.close()
    return data


def list_to_df():
    qu = '新郑市'
    name = f'{qu}_town'
    name1 = 'community'
    # 列表
    community_name_list = get_Zhengzhou()
    for i in range(len(community_name_list)):

        # list转dataframe
        df = pd.DataFrame(community_name_list[i], columns=[f'{name1}_name'])   #社区

        # 保存到本地csv
        df.to_csv(f"../data/{qu}/{name}_{name1}{i}_name.csv", index=False)




if __name__ == "__main__":
    list_to_df()
    # get_Zhengzhou()





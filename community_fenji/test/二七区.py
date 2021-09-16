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
    ids = 410103   #二七区
    data = []
    'http://www.syx7.com/Citydm.asp?Field=AreaCode&dm=410103014&keyword=%BA%D3%C4%CF%CA%A1%D6%A3%D6%DD%CA%D0%D0%C2%D6%A3%CA%D0'
    # kw = '&keyword=%BA%D3%C4%CF%CA%A1%D6%A3%D6%DD%CA%D0%D0%C2%D6%A3%CA%D0'
    # 'http://www.syx7.com/Citydm.asp?Field=AreaCode&dm=410103003{}'.format(kw)
    id_list = [*range(1,14)]
    id_list.append(100)
    id_list.append(201)
    # print(id_list)
    for id in id_list:
        if id < 10:
            url1 = f"http://www.syx7.com/Citydm.asp?Field=AreaCode&dm={ids}00{id}&keyword=%BA%D3%C4%CF%CA%A1%D6%A3%D6%DD%CA%D0%D0%C2%D6%A3%CA%D0"
        elif 10<=id<14:
            url1 = f"http://www.syx7.com/Citydm.asp?Field=AreaCode&dm={ids}0{id}&keyword=%BA%D3%C4%CF%CA%A1%D6%A3%D6%DD%CA%D0%D0%C2%D6%A3%CA%D0"
        else:
            url1 = f"http://www.syx7.com/Citydm.asp?Field=AreaCode&dm={ids}{id}&keyword=%BA%D3%C4%CF%CA%A1%D6%A3%D6%DD%CA%D0%D0%C2%D6%A3%CA%D0"

        browser.get(url1)

        # 和邮政编码有关  还是先将数据汇总成数据表 /html/body/table[3]/tbody/tr[4]/td[1]/a 1
        # /html/body/table[3]/tbody/tr[5]/td[1]/a 3
        if id == 1 or id == 9:
            data1=[]
            for i in range(4,15):
                #获取林山寨街道办事处下得社区名称
                c = browser.find_element_by_xpath(f'/html/body/table[3]/tbody/tr[{i}]/td[1]/a')
                data1.append(c.text)
            data.append(data1)
        elif id == 2 :
            data2=[]
            for i in range(4,5):
                #获取林山寨街道办事处下得社区名称
                c = browser.find_element_by_xpath(f'/html/body/table[3]/tbody/tr[{i}]/td[1]/a')
                data2.append(c.text)
            data.append(data2)
        elif id == 3:
            data3=[]
            for i in range(4,10):
                #获取林山寨街道办事处下得社区名称
                c = browser.find_element_by_xpath(f'/html/body/table[3]/tbody/tr[{i}]/td[1]/a')
                data3.append(c.text)
            data.append(data3)
        elif id == 4:
            data5=[]
            for i in range(4,8):
                #获取林山寨街道办事处下得社区名称
                c = browser.find_element_by_xpath(f'/html/body/table[3]/tbody/tr[{i}]/td[1]/a')
                data5.append(c.text)
            data.append(data5)
        elif id == 5 :
            data0=[]
            for i in range(4,9):
                #获取林山寨街道办事处下得社区名称
                c = browser.find_element_by_xpath(f'/html/body/table[3]/tbody/tr[{i}]/td[1]/a')
                data0.append(c.text)
            data.append(data0)
        elif id == 6:
            data0=[]
            for i in range(4,21):
                #获取林山寨街道办事处下得社区名称
                c = browser.find_element_by_xpath(f'/html/body/table[3]/tbody/tr[{i}]/td[1]/a')
                data0.append(c.text)
            data.append(data0)
        elif id == 7:
            data0=[]
            for i in range(4,16):
                #获取林山寨街道办事处下得社区名称
                c = browser.find_element_by_xpath(f'/html/body/table[3]/tbody/tr[{i}]/td[1]/a')
                data0.append(c.text)
            data.append(data0)
        elif id == 8 or id == 11:
            data0=[]
            for i in range(4,18):
                #获取林山寨街道办事处下得社区名称
                c = browser.find_element_by_xpath(f'/html/body/table[3]/tbody/tr[{i}]/td[1]/a')
                data0.append(c.text)
            data.append(data0)
        elif id == 10:
            data0=[]
            for i in range(4,7):
                #获取林山寨街道办事处下得社区名称
                c = browser.find_element_by_xpath(f'/html/body/table[3]/tbody/tr[{i}]/td[1]/a')
                data0.append(c.text)
            data.append(data0)
        elif id == 12 or id == 13:
            data0=[]
            for i in range(4,12):
                #获取林山寨街道办事处下得社区名称
                c = browser.find_element_by_xpath(f'/html/body/table[3]/tbody/tr[{i}]/td[1]/a')
                data0.append(c.text)
            data.append(data0)
        elif id == 100:
            data0=[]
            for i in range(4,17):
                #获取林山寨街道办事处下得社区名称 /html/body/table[3]/tbody/tr[4]/td[1]/a
                #/html/body/table[3]/tbody/tr[5]/td[1]/a
                c = browser.find_element_by_xpath(f'/html/body/table[3]/tbody/tr[{i}]/td[1]/a')
                data0.append(c.text)
            data.append(data0)
        elif id == 201:
            data0=[]
            for i in range(4,32):
                #获取林山寨街道办事处下得社区名称
                c = browser.find_element_by_xpath(f'/html/body/table[3]/tbody/tr[{i}]/td[1]/a')
                data0.append(c.text)
            data.append(data0)
        else:
            break
    url = 'http://www.syx7.com/Citydm.asp?Field=AreaCode&dm=410103100&keyword=%BA%D3%C4%CF%CA%A1%D6%A3%D6%DD%CA%D0%B6%FE%C6%DF%C7%F8%C2%ED%D5%AF%D5%F2'


    print(data)
    print(len(data))
    browser.close()
    return data


def list_to_df():
    qu = '二七区'
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





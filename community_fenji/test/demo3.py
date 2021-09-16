# codeing : utf-8
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/8/25 0:22
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

    #中原区 看来是不能大规模成批得获取了，只能单独获取页面了。
    # urlid = [410102,410103,410104,410105,410106,410108,410122,410181,410182,410183,410184,410185]
    id = 4101020
    data = []
    for id in range(1,13):
        if id < 10:
            url1 = f"http://www.syx7.com/Citydm.asp?Field=AreaCode&dm=41010200{id}&keyword=%BA%D3%C4%CF%CA%A1%D6%A3%D6%DD%CA%D0%D0%C2%D6%A3%CA%D0"
        else:
            url1 = f"http://www.syx7.com/Citydm.asp?Field=AreaCode&dm=4101020{id}&keyword=%BA%D3%C4%CF%CA%A1%D6%A3%D6%DD%CA%D0%D0%C2%D6%A3%CA%D0"
        browser.get(url1)

        # 和邮政编码有关  还是先将数据汇总成数据表 /html/body/table[3]/tbody/tr[4]/td[1]/a
        # /html/body/table[3]/tbody/tr[5]/td[1]/a
        if id == 1 or id == 10:
            data1=[]
            for i in range(4,18):
                #获取林山寨街道办事处下得社区名称
                c = browser.find_element_by_xpath(f'/html/body/table[3]/tbody/tr[{i}]/td[1]/a')
                data1.append(c.text)
            data.append(data1)
        elif id == 2 or id == 4:
            data2=[]
            for i in range(4,12):
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
        elif id == 5:
            data5=[]
            for i in range(4,24):
                #获取林山寨街道办事处下得社区名称
                c = browser.find_element_by_xpath(f'/html/body/table[3]/tbody/tr[{i}]/td[1]/a')
                data5.append(c.text)
            data.append(data5)
        elif id == 6 or id == 12:
            data0=[]
            for i in range(4,17):
                #获取林山寨街道办事处下得社区名称
                c = browser.find_element_by_xpath(f'/html/body/table[3]/tbody/tr[{i}]/td[1]/a')
                data0.append(c.text)
            data.append(data0)
        elif id == 7 or id == 9:
            data0=[]
            for i in range(4,16):
                #获取林山寨街道办事处下得社区名称
                c = browser.find_element_by_xpath(f'/html/body/table[3]/tbody/tr[{i}]/td[1]/a')
                data0.append(c.text)
            data.append(data0)
        elif id == 8:
            data0=[]
            for i in range(4,20):
                #获取林山寨街道办事处下得社区名称
                c = browser.find_element_by_xpath(f'/html/body/table[3]/tbody/tr[{i}]/td[1]/a')
                data0.append(c.text)
            data.append(data0)
        elif id == 11:
            data0=[]
            for i in range(4,14):
                #获取林山寨街道办事处下得社区名称
                c = browser.find_element_by_xpath(f'/html/body/table[3]/tbody/tr[{i}]/td[1]/a')
                data0.append(c.text)
            data.append(data0)

        else:
           break

    print(data)
    print(len(data))
    browser.close()
    return data


def list_to_df():
    name = '中原区_town'
    name1 = 'community'
    # 列表
    community_name_list = get_Zhengzhou()
    for i in range(len(community_name_list)):

        # list转dataframe
        df = pd.DataFrame(community_name_list[i], columns=[f'{name1}_name'])   #社区

        # 保存到本地csv
        df.to_csv(f"../data/{name}_{name1}{i}_name.csv", index=False)




if __name__ == "__main__":
    list_to_df()
    # get_Zhengzhou()



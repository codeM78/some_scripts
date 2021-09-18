# -*- coding:gbk -*-

import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from private_info import *
import mail


def sign_in(uid, pwd):

    # set to no-window
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")

    # simulate a browser to open the website
    browser = webdriver.Chrome(options=chrome_options
                                #这里记得配置自己的浏览器驱动
                               ,executable_path="../zhengzhou_community/chromedriver.exe")
    # browser = webdriver.Chrome()
    # 连接被浏览器提示为不安全，添加白名单即可
    browser.get("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0")

    # input uid and password
    # //*[@id="mt_5"]/div[2]/div[3]/input  //*[@id="mt_5"]/div[3]/div[3]/input
    print("Inputting the UID and Password of User {0}".format(uid))
    # 半夜12点多进不去了--（不知道由于什么原因），可能定位不到，加个轮询和异常处理--依旧是不行。这种爬取网站的时候有延时风险
    while 1:
        start = time.time()
        try:
            browser.find_element_by_xpath('//*[@id="mt_5"]/div[2]/div[3]/input').send_keys(uid)
            browser.find_element_by_xpath('//*[@id="mt_5"]/div[3]/div[3]/input').send_keys(pwd)
            print('已定位到元素')
            end = time.time()
            break
        except:
            print("还未定位到元素!")
    print('定位耗费时间：'+str(end-start))

    # click to sign in  点击登录
    # //*[@id="mt_5"]/div[5]/div/input

    browser.find_element_by_xpath("//*[@id='mt_5']/div[5]/div/input").click()
    time.sleep(3)

    # get middle info
    real_mid_page_url = browser.find_element_by_xpath("//*[@id='zzj_top_6s']").get_attribute("src")
    browser.get(real_mid_page_url)

    print("Checking whether User {0} has signed in".format(uid))
    msg = browser.find_element_by_xpath("//*[@id='bak_0']/div[7]/span").text
    # 如果今日填报郭就退出填报，直接返回msg
    if msg == "今日您已经填报过了":
        return msg

    # click to fill in
    # # 适配填报健康码绿码和疫苗接种两针，其实不做新的适配也能’伪‘打卡--打卡成功（虽然信息提示失败）
    # # 健康码绿码--
    # # 1.点击候选框
    # browser.find_element_by_xpath('//*[@id="bak_0"]/div[8]/div[2]/div[2]/div[2]/select[1]').click()
    # time.sleep(1)
    # # 2.点击绿码
    # browser.find_element_by_xpath('//*[@id="bak_0"]/div[8]/div[2]/div[2]/div[2]/select[1]/option[2]').click()
    #
    # # 疫苗接种两针
    # # 1.点击选框
    # browser.find_element_by_xpath('//*[@id="bak_0"]/div[8]/div[2]/div[2]/div[2]/div[2]/select/option[3]').click()
    # time.sleep(1)
    # # 2.点击两针接种
    # browser.find_element_by_xpath('//*[@id="bak_0"]/div[8]/div[2]/div[2]/div[2]/div[2]/select/option[3]').click()

    # 点击填报
    span_text = browser.find_element_by_xpath("//*[@id='bak_0']/div[13]/div[3]/div[4]/span").text
    if span_text == "本人填报":
        browser.find_element_by_xpath("//*[@id='bak_0']/div[13]/div[3]/div[4]").click()
    else:
        browser.find_element_by_xpath("//*[@id='bak_0']/div[13]/div[3]/div[6]").click()

    time.sleep(2)

    # click to submit
    print("Signing in for User {0}".format(uid))
    # 这里定位不对了又  //*[@id="bak_0"]/div[8]/div[2]/div[2]/div[2]/div[6]/div[4]/span
    browser.find_element_by_xpath('//*[@id="bak_0"]/div[8]/div[2]/div[2]/div[2]/div[6]/div[4]/span').click()
    # browser.find_element_by_xpath("//*[@id='bak_0']/div[19]/div[4]").click()
    time.sleep(2)

    final_text = browser.find_element_by_xpath("//*[@id='bak_0']/div[2]/div[2]/div[2]/div[2]").text

    # quit the browser
    print("Singing in for User {0} is finished".format(uid))
    browser.quit()
    return final_text


if __name__ == "__main__":

    # For Single User
    pass
    msg = sign_in(UID, PWD)
    # # 发送邮件信息
    mail.mail(msg, MAIL_TO)

    # For Multiple Users
    # while True:
    #     while True:
    #         now = datetime.datetime.now()
    #         # 修改定时
    #         if now.hour == 6 and now.minute == 0:
    #             break
    #         time.sleep(30)
    #
    #     for user in users:
    #         msg = sign_in(user.uid, user.pwd)
    #         print("Emailing to User {0} for notification".format(user.uid))
    #         mail.mail(msg, user.email)
    #         print("Emailing is finished")

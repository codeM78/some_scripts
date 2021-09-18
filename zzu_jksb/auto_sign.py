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
                                #����ǵ������Լ������������
                               ,executable_path="../zhengzhou_community/chromedriver.exe")
    # browser = webdriver.Chrome()
    # ���ӱ��������ʾΪ����ȫ����Ӱ���������
    browser.get("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0")

    # input uid and password
    # //*[@id="mt_5"]/div[2]/div[3]/input  //*[@id="mt_5"]/div[3]/div[3]/input
    print("Inputting the UID and Password of User {0}".format(uid))
    # ��һ�����ȥ��--��������ԭ�򣬿��ܶ�λ�������Ӹ���ѯ���쳣����--�����ǲ��С�������ȡ��վ��ʱ������ʱ����
    while 1:
        start = time.time()
        try:
            browser.find_element_by_xpath('//*[@id="mt_5"]/div[2]/div[3]/input').send_keys(uid)
            browser.find_element_by_xpath('//*[@id="mt_5"]/div[3]/div[3]/input').send_keys(pwd)
            print('�Ѷ�λ��Ԫ��')
            end = time.time()
            break
        except:
            print("��δ��λ��Ԫ��!")
    print('��λ�ķ�ʱ�䣺'+str(end-start))

    # click to sign in  �����¼
    # //*[@id="mt_5"]/div[5]/div/input

    browser.find_element_by_xpath("//*[@id='mt_5']/div[5]/div/input").click()
    time.sleep(3)

    # get middle info
    real_mid_page_url = browser.find_element_by_xpath("//*[@id='zzj_top_6s']").get_attribute("src")
    browser.get(real_mid_page_url)

    print("Checking whether User {0} has signed in".format(uid))
    # msg = browser.find_element_by_xpath("//*[@id='bak_0']/div[7]/span").text
    # if msg == "�������Ѿ������":
    #     return msg

    # click to fill in
    # ��������������������������룬��ʵ�����µ�����Ҳ�ܡ�α����--�򿨳ɹ�
    # ����������
    time.sleep(1)
    # hc = browser.find_element_by_tag_name('option')[2]
    hc = browser.find_element_by_xpath('//*[@id="bak_0"]/div[8]/div[2]/div[2]/div[2]/select[1]/option[2]').text

    # �����������
    time.sleep(1)
    # ym = browser.find_element_by_tag_name('option')[6]
    ym = browser.find_element_by_xpath('//*[@id="bak_0"]/div[8]/div[2]/div[2]/div[2]/div[2]/select/option[3]').text

    ����
    span_text = browser.find_element_by_xpath("//*[@id='bak_0']/div[13]/div[3]/div[4]/span").text
    if span_text == "�����":
        browser.find_element_by_xpath("//*[@id='bak_0']/div[13]/div[3]/div[4]").click()
    else:
        browser.find_element_by_xpath("//*[@id='bak_0']/div[13]/div[3]/div[6]").click()

    time.sleep(2)

    # click to submit
    print("Signing in for User {0}".format(uid))
    # ���ﶨλ��������  //*[@id="bak_0"]/div[8]/div[2]/div[2]/div[2]/div[6]/div[4]/span
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
    # # �����ʼ���Ϣ
    mail.mail(msg, MAIL_TO)

    # For Multiple Users
    # while True:
    #     while True:
    #         now = datetime.datetime.now()
    #         # �޸Ķ�ʱ
    #         if now.hour == 6 and now.minute == 0:
    #             break
    #         time.sleep(30)
    #
    #     for user in users:
    #         msg = sign_in(user.uid, user.pwd)
    #         print("Emailing to User {0} for notification".format(user.uid))
    #         mail.mail(msg, user.email)
    #         print("Emailing is finished")

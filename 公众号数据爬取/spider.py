# -*- codeing: utf-8 -*-
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/8/20 14:59
# @Software: PyCharm

from bs4 import BeautifulSoup   #网页解析，获取数据
import re   #正则表达式，进行文字匹配
from urllib import request,error    #指定URL，获取网页数据
import xlwt #进行excel操作
import sqlite3  #进行SQLite数据库操作


#影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">') #创建正则表达式对象，表示规则（字符串的模式）
#影片图片
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S) #re.S让换行符包含在字符中
#影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
#影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
#找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
#找到影片相关的内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)   #re.S让换行符包含在所选字符中


#爬取网页--用来获取多个网页
def getData(baseurl):
    datalist = []
    for i in range(10):
        url = baseurl + str(i*25)
        html = askURL(url)  #保存获取到的网页源码

        # 2. 逐一解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all("div",class_="item"): #查找符合要求的字符串，形成列表
            data = []   #保存一部电影所有的重要信息
            item = str(item)

            #获取影片详情的链接
            link = re.findall(findLink,item)[0] #用正则表达式查找指定的字符串
            data.append(link)

            imgSrc = re.findall(findImgSrc,item)[0] #获取图片
            data.append(imgSrc)

            titles = re.findall(findTitle,item) #有可能不存在外文名
            if len(titles) == 2:
                ctitle = titles[0]
                data.append(ctitle) #获取中文名
                otitle = titles[1].replace("/","")  #去掉无关的符号
                data.append(otitle) #获取外文名
            else:
                data.append(titles[0])
                data.append(" ")    #外国名留空

            rating = re.findall(findRating,item)[0] #获取评分
            data.append(rating)

            judgeNum = re.findall(findJudge,item)[0]    #获取评价人数
            data.append(judgeNum)

            inq = re.findall(findInq,item)  #有可能不存在简介
            if len(inq) != 0:
                inq = inq[0].replace("。", "")   #去掉句号
                data.append(inq)
            else:
                data.append(" ")    #没有简介的话留空

            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s)?'," ",bd)  #去掉<br/>
            bd = re.sub('/'," ",bd) #替换/
            data.append(bd.strip()) #strip()去掉字符串前后的空格

            datalist.append(data)   # 把处理好的一部电影信息放入datalist

    return datalist

#获取指定一个URL的网页内容
def askURL(url):
    #模拟浏览器头部信息，向豆瓣服务器发送消息
    headers = {
        #用户代理，告诉豆瓣服务器，访问者时什么类型的机器、浏览器
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"
    }
    req = request.Request(url,headers=headers)
    #定义空字符串html
    html = ""
    try:
        response = request.urlopen(req)
        html = response.read().decode("utf-8")
        # print(html)
    except error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html


#保存数据到excel
def saveData(datalist,savepath):
    workbook = xlwt.Workbook(encoding='utf-8',style_compression=0)
    worksheet = workbook.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)
    col = ("影片详情链接","图片链接","影片中文名称","影片外文名称","评分","评价人数","影片概况","相关信息")  #定义了一个元组
    for i in range(len(col)):
        worksheet.write(0,i,col[i]) #第一行写入列名
    for i in range(len(datalist)):
        print(f"第{i+1}条信息已保存")
        data = datalist[i]
        for j in range(len(data)):
            worksheet.write(i+1,j,data[j])

    workbook.save(savepath)


#保存数据到数据库
def saveData2DB(datalist,dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    #只要涉及写磁盘就要记得异常处理
    for data in datalist:   #遍历行
        for index in range(len(data)):  #遍历列
            if index == 4 or index == 5:    #索引4，5保留原来的numeric格式
                continue
            data[index] = '"'+data[index]+'"'   #为其余数据加上双引号
        sql = r'''
            insert into movie_top250(
            info_link, pic_link, cname, ename, score, rated, instroductionn, info
            ) values ({})'''.format(','.join(data))
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()



#初始化数据库，数据表
def init_db(dbpath):
    # 用来创建数据表的语句
    sql = '''
        create table movie_top250(
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar ,
        ename varchar ,
        score numeric ,
        rated numeric ,
        instroductionn text,
        info text
        
        )
    
    '''
    conn = sqlite3.connect(dbpath)  #如果存在数据库就连接，否则就创建
    cursor = conn.cursor()  #创建游标
    cursor.execute(sql)
    conn.commit()   #提交
    conn.close()


def get_top250():
    baseurl = "https://movie.douban.com/top250?start="
    # 1. 爬取网页
    datalist = getData(baseurl)
    # 3. 保存数据

    # savepath = r"D:\Python works\douban\data\DoubanMovies_Top250.xls" #保存到本地为excel
    # saveData(datalist,savepath)

    dbpath = r"D:\Python works\douban\data\movie.db"    #保存到数据库
    saveData2DB(datalist,dbpath)


#定义主方法，程序入口
if __name__ == "__main__":
    get_top250()
    print('爬取并保存数据完成！')
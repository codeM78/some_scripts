# coding=utf-8
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/9/11 16:50
# @Software: PyCharm


def main():
    # Todo: Add your code here
    pass
    list1 = [1, 3, 5, 7, 100]
    # 添加元素
    list1.append(200)
    list1.insert(1, 400)
    # print(list1)

    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    # 列表切片
    fruits2 = fruits[1:4]
    # print(fruits2) # apple strawberry waxberry
    # 可以通过完整切片操作来复制列表--直接赋值也是一样的
    # fruits3 = fruits[:]
    fruits3 = fruits
    print(fruits3) # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
    # fruits4 = fruits[-3:-1]
    # print(fruits4) # ['pitaya', 'pear']
    # # 可以通过反向切片操作来获得倒转后的列表的拷贝
    # fruits5 = fruits[::-1]
    # print(fruits5) # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']

    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1)
    # sorted函数返回列表排序后的拷贝不会修改传入的列表
    # 函数的设计就应该像sorted函数一样尽可能不产生副作用
    list3 = sorted(list1, reverse=True)
    # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
    list4 = sorted(list1, key=len)
    # print(list1)
    # print(list2)
    # print(list3)
    # print(list4)
    # # 给列表对象发出排序消息直接在列表对象上进行排序
    # list1.sort(reverse=True)
    # print(list1)

    f = [x for x in range(1, 10)]
    print(f)
    f = [x + y for x in 'ABCDE' for y in '1234567']  #列表生成式就是好用
    print(f)

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a  #使用yield关键字将一个普通函数改造成生成器函数


def main1():
    for val in fib(20):
        print(val)


def jiHe():
    # 创建集合的字面量语法
    set1 = {1, 2, 3, 3, 3, 2}
    print(set1)
    print('Length =', len(set1))
    # 创建集合的构造器语法(面向对象部分会进行详细讲解)
    set2 = set(range(1, 10))
    set3 = set((1, 2, 3, 3, 2, 1))
    print(set2, set3)
    # 创建集合的推导式语法(推导式也可以用于推导集合)
    set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
    print(set4)

    # 向集合添加元素和从集合删除元素。
    set1.add(4)
    set1.add(5)
    set2.update([11, 12])
    set2.discard(5)
    if 4 in set2:
        set2.remove(4)
    print(set1, set2)
    print(set3.pop()) #删除一个元素，其实就是栈顶元素
    print(set3)

    print('---------------------------------------------------')
    # 集合的交集、并集、差集、对称差运算
    print(set1,set2,set3)
    print(set1 & set2)
    # print(set1.intersection(set2))
    print(set1 | set2)
    # print(set1.union(set2))
    print(set1 - set2)
    # print(set1.difference(set2))
    print(set1 ^ set2)  #交集的补集OR并集-交集
    # print(set1.symmetric_difference(set2))
    # 判断子集和超集
    print(set2 <= set1)
    # print(set2.issubset(set1))
    print(set3 <= set1)
    # print(set3.issubset(set1))
    print(set1 >= set2)
    # print(set1.issuperset(set2))
    print(set1 >= set3)
    # print(set1.issuperset(set3))

def dictionary():
    # 创建字典的字面量语法
    scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
    print(scores)
    # 创建字典的构造器语法
    items1 = dict(one=1, two=2, three=3, four=4)
    # 通过zip函数将两个序列压成字典
    items2 = dict(zip(['a', 'b', 'c'], '123'))
    # 创建字典的推导式语法
    items3 = {num: num ** 2 for num in range(1, 10)}
    # print(items1, items2, items3)
    # 通过键可以获取字典中对应的值
    print(scores['骆昊'])
    print(scores['狄仁杰'])
    # 对字典中所有键值对进行遍历
    for key in scores:
        print(f'{key}: {scores[key]}')
    # 更新字典中的元素--添加元素
    scores['白元芳'] = 65
    scores['诸葛王朗'] = 71
    scores.update(冷面=67, 方启鹤=85)
    print(scores)

# 练习1:跑马灯文字
def paoMaDeng(): #跑马灯文字
    import os
    import time

    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]

# 练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
def generate_code(code_len=4):

    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    import random

    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code

# 练习3：设计一个函数返回给定文件名的后缀名。
def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''

# 练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。
def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    #遍历出最大值和次大值
    for index in range(2, len(x)):
        #m1是当前最大值，m2是当前次大值
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2

# 练习5：计算指定的年月日是这一年的第几天。
def is_leap_year(year):
    """
    判断指定的年份是不是闰年

    :param year: 年份
    :return: 闰年返回True平年返回False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, date):
    """
    计算传入的日期是这一年的第几天

    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]  #用布尔值代替索引0和1
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date

def main2():
    print(which_day(1980, 11, 28))
    print(which_day(1981, 12, 31))
    print(which_day(1999, 8, 29))
    print(which_day(2000, 7, 19))
    print(which_day(2018, 1, 1))
    print(which_day(2016, 3, 1))

# 练习6：打印杨辉三角。
def yangHui():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()

# 综合案例
# 案例1：双色球选号。



def display(balls):
    """
    输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    """
    from random import randrange, randint, sample

    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def main3():

    n = int(input('机选几注: '))
    for _ in range(n):
        display(random_select())

# 综合案例2：约瑟夫环问题。
"""
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，
有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，
报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，
哪些位置是基督徒哪些位置是非基督徒。
"""

def main4():
    persons = [True] * 30  #设定30个True
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end='')

# 综合案例3：井字棋游戏。


def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


def main5():
    import os

    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        # os.system('cls')  #win下的清屏函数
        # os.system('clear')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            # os.system('cls')
            # os.system('clear')
            print_board(curr_board)
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'

if __name__ == '__main__':
    # main()
    # main1()
    # jiHe()
    # dictionary()
    # paoMaDeng()

    # code = generate_code()
    # print(code)
    # print(get_suffix('test.html', has_dot=True))
    # print(max2([888,2,300.4,7,87]))
    # main2()

    # yangHui()
    # main3()
    # main4()
    main5()
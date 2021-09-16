# coding=utf-8
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/9/12 19:10
# @Software: PyCharm

def main():
    try:
        with open('致橡树.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')

import time
def main1():
    # 一次性读取整个文件内容
    with open('致橡树.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('致橡树.txt', mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open('致橡树.txt', encoding='utf-8') as f:
        lines = f.readlines()
    print(lines)

# 读写二进制文件
def main2():
    try:
        with open('guido.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # <class 'bytes'>
        with open('吉多.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开.')
    except IOError as e:
        print('读写文件时出现错误.')
    print('程序执行结束.')

# 读写JSON文件
import json


def main_json():
    mydict = {
        'name': '铭同学',
        'age': 22,
        'qq': 124353,
        'friends': ['李元芳', '奥特曼'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            # ensure_ascii=False正常显示中文
            json.dump(mydict, fs, ensure_ascii=False)

    except IOError as e:
        print(e)
    print('保存数据完成!')



if __name__ == '__main__':
    pass
    # main()
    # main1()
    # main2()

    main_json()
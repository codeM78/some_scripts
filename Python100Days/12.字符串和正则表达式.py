# coding=utf-8
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/9/12 23:34
# @Software: PyCharm
import re

# 例子1：验证输入用户名和QQ号是否有效并给出对应的提示信息。
"""
验证输入用户名和QQ号是否有效并给出对应的提示信息
要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""
def main():
    username = input('请输入用户名: ')
    qq = input('请输入QQ号: ')
    # match函数的第一个参数是正则表达式字符串或正则表达式对象
    # 第二个参数是要跟正则表达式做匹配的字符串对象
    #匹配用户名的正则表达式
    # username_ = re.compile(r'^[0-9a-zA-Z_]{6,20}$')
    username_pattern = re.compile(r'^\w{6,20}$')
    m1 = re.match(username_pattern, username)
    if not m1:
        print('请输入有效的用户名.')
    #匹配qq的正则表达式
    # qq_ = re.compile(r'^[1-9]\d{4,11}$')
    qq_pattern = re.compile(r'^[1-9]\d{4,11}$')
    m2 = re.match(qq_pattern, qq)
    if not m2:
        print('请输入有效的QQ号.')
    if m1 and m2:
        print('你输入的信息是有效的!')


# 例子2：从一段文字中提取出国内手机号码。
def main1():
    # 创建正则表达式对象 使用了前瞻和回顾来保证手机号前后不应该出现数字
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也不是110或119，王大锤的手机号才是15600998765。
    '''
    # 查找所有匹配并保存到一个列表中
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('--------华丽的分隔线--------')
    # 通过迭代器取出匹配对象并获得匹配的内容
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('--------华丽的分隔线--------')
    # 通过search函数指定搜索位置找出所有匹配
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())

# 例子3：替换字符串中的不良内容
def main2():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                      '*', sentence, flags=re.IGNORECASE)
    print(purified)  # 你丫是*吗? 我*你大爷的. * you.

# 例子4：拆分长字符串
def main3():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。, .]', poem)
    #删除''引号
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)  # ['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡']


if __name__ == '__main__':
    pass
    # main()
    # main1()
    # main2()
    main3()

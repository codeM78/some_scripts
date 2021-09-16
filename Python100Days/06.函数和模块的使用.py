# coding=utf-8
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/9/11 16:17
# @Software: PyCharm

# 组合运算，输入M和N计算C(M,N)
# 求阶乘重复计算（3次），应该进行封装
def C_M_N():
    m = int(input('m = '))
    n = int(input('n = '))
    fm = 1 #求m阶乘
    for num in range(1, m + 1):
        fm *= num
    fn = 1 #求n阶乘
    for num in range(1, n + 1):
        fn *= num
    fm_n = 1 #求（m-n）的阶乘
    for num in range(1, m - n + 1):
        fm_n *= num
    print(fm // fn // fm_n)

#封装阶乘运算
# Python的math模块中其实已经有一个名为factorial函数实现了阶乘运算
def jieCheng(num:int):
    result = 1
    for i in range(1,num+1):
        result *= i
    return result

def btetter_C_M_N():
    m = int(input('m = '))
    n = int(input('n = '))
    # 当需要计算阶乘的时候不用再写循环求阶乘而是直接调用已经定义好的函数
    print(jieCheng(m) // jieCheng(n) // jieCheng(m-n))








if __name__ == '__main__':
    pass
    # C_M_N()
    btetter_C_M_N()
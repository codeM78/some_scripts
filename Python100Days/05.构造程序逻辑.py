# coding=utf-8
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/9/11 13:01
# @Software: PyCharm

# 案例1：寻找水仙花数
# 说明：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，
# 它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。
def shuiXianHua():
    for num in range(100,1000):   #限制3位数
        low = num % 10  #获取个位数
        mid = num // 10 % 10  #获取十位数
        high = num // 100  #获取百位数
        # 每个位上数字的立方之和正好等于它本身
        if low**3 + mid**3 + high**3 == num:
            print(num)

# 案例2：正整数的反转
def intReverse():
    num = int(input('num = '))
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10  #顺利实现减少位数
    print(reversed_num)

# 案例3：百钱百鸡问题。
# 说明：百钱百鸡是我国古代数学家张丘建在《算经》一书中提出的数学问题：
# 鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
# 翻译成现代文是：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
def baiJi():  #使用得是暴力破解法（穷举法）
    for x in range(0, 20):
        for y in range(0, 33):
            z = 100 - x - y
            if 5 * x + 3 * y + z / 3 == 100:
                print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))

# 案例4：CRAPS赌博游戏。
# 说明：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
# 该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
# 简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；
# 其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；
# 其他点数，玩家继续要骰子，直到分出胜负。
def CRAPS():
    """
    Craps赌博游戏
    我们设定玩家开始游戏时有1000元的赌注
    游戏结束的条件是玩家输光所有的赌注

    """
    from random import randint

    money = 1000
    while money > 0:
        print('你的总资产为:', money)
        needs_go_on = False
        while True:
            debt = int(input('请下注: '))
            if 0 < debt <= money:
                break
        first = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % first)
        if first == 7 or first == 11:
            print('玩家胜!')
            money += debt
        elif first == 2 or first == 3 or first == 12:
            print('庄家胜!')
            money -= debt
        else:
            needs_go_on = True
        while needs_go_on:
            needs_go_on = False
            current = randint(1, 6) + randint(1, 6)
            print('玩家摇出了%d点' % current)
            if current == 7:
                print('庄家胜')
                money -= debt
            elif current == first:
                print('玩家胜')
                money += debt
            else:
                needs_go_on = True
    print('你破产了, 游戏结束!')



'''练习部分'''
# 练习1：生成斐波那契数列的前20个数。
# 说明：斐波那契数列（Fibonacci sequence），又称黄金分割数列，是意大利数学家莱昂纳多·斐波那契
# （Leonardoda Fibonacci）在《计算之书》中提出一个在理想假设条件下兔子成长率的问题而引入的数列，
# 所以这个数列也被戏称为"兔子数列"。斐波那契数列的特点是数列的前两个数都是1，
# 从第三个数开始，每个数都是它前面两个数的和，形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。
# 斐波那契数列在现代物理、准晶体结构、化学等领域都有直接的应用。
def fibonacci_20():
    num1 = 1
    num2 = 1
    print(num1,num2,end=' ')
    for i in range(18):
        num = num1+num2
        num1 = num2
        num2 = num
        print(num,end=' ')


# 练习2：找出10000以内的完美数。 6，28，496，8128
# 说明：完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
# 例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。完美数有很多神奇的特性，有兴趣的可以自行了解。
def perfectNum_10000():
    print('10000以内得完美数有：',end='')
    for num in range(1,10001):

        # 获取除去自身外的真因子
        sum=0  #用于存储真因子的和
        for i in range(1,num):
            if num%i == 0:
                sum += i
        #num一轮的因子加和最终完成后再进行判断
        if sum == num:
            print(num,end=' ')

# 练习3：输出100以内所有的素数。
# 说明：素数指的是只能被1和自身整除的正整数（不包括1）。
def primeNum_100():
    print('100以内得素数有：',end='')
    for num in range(2,101):
        # 获取除去自身外的真因子
        sum=0  #用于存储真因子的和
        for i in range(1,num):
            if num%i == 0:
                sum += i
        #num一轮的因子加和最终完成后再进行判断,若真因子之和为1
        if sum == 1:
            print(num,end=' ')







if __name__ =='__main__':
    pass
    # shuiXianHua()
    # intReverse()
    # baiJi()
    # CRAPS()
    # fibonacci_20()
    # perfectNum_10000()
    primeNum_100()
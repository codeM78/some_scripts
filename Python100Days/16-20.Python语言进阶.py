# coding=utf-8
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/9/14 12:06
# @Software: PyCharm



def main():
    # Todo: Add your code here
    pass
    # 生成式（推导式）的用法
    # 说明：生成式（推导式）可以用来生成列表、集合和字典。
    prices = {
        'AAPL': 191.88,
        'GOOG': 1186.96,
        'IBM': 149.24,
        'ORCL': 48.44,
        'ACN': 166.89,
        'FB': 208.09,
        'SYMC': 21.29
    }
    # 用股票价格大于100元的股票构造一个新的字典
    prices2 = {key:value for key, value in prices.items() if value > 100}
    print(prices2)

def list():
    #列表嵌套的坑
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    courses = ['语文', '数学', '英语']
    # 录入五个学生三门课程的成绩
    # 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
    # scores = [[None] * len(courses)] * len(names)
    scores = [[None] * len(courses) for _ in range(len(names))]
    for row, name in enumerate(names):
        for col, course in enumerate(courses):
            scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
            print(scores)

def heap():
    """
    从列表中找出最大的或最小的N个元素
    堆结构(大根堆/小根堆)
    """
    import heapq

    list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
    list2 = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    print(heapq.nlargest(3, list1))
    print(heapq.nsmallest(3, list1))
    print(heapq.nlargest(2, list2, key=lambda x: x['price']))
    print(heapq.nlargest(2, list2, key=lambda x: x['shares']))

# itertools模块
def itertool():
    """
    迭代工具模块
    """
    import itertools

    # 产生ABCD的全排列
    print([*itertools.permutations('ABCD')])
    # 产生ABCDE的五选三组合
    itertools.combinations('ABCDE', 3)
    # 产生ABCD和123的笛卡尔积
    print([*itertools.product('ABCD', '123')])
    # 产生ABC的无限循环序列
    itertools.cycle(('A', 'B', 'C'))

# collections模块
# 常用的工具类：
'''
namedtuple：命令元组，它是一个类工厂，接受类型的名称和属性列表来创建一个类。
deque：双端队列，是列表的替代实现。Python中的列表底层是基于数组来实现的，而deque底层是双向链表，因此当你需要在头尾添加和删除元素是，deque会表现出更好的性能，渐近时间复杂度为$O(1)$。
Counter：dict的子类，键是元素，值是元素的计数，它的most_common()方法可以帮助我们获取出现频率最高的元素。Counter和dict的继承关系我认为是值得商榷的，按照CARP原则，Counter跟dict的关系应该设计为关联关系更为合理。
OrderedDict：dict的子类，它记录了键值对插入的顺序，看起来既有字典的行为，也有链表的行为。
defaultdict：类似于字典类型，但是可以通过默认的工厂函数来获得键对应的默认值，相比字典中的setdefault()方法，这种做法更加高效。
'''
def collection():
    """
    找出序列中出现次数最多的元素
    """
    from collections import Counter

    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
        'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
        'look', 'into', 'my', 'eyes', "you're", 'under'
    ]
    counter = Counter(words)
    print(counter.most_common(3))

# 排序算法（选择、冒泡和归并）和查找算法（顺序和折半）
def select_sort(items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items

def bubble_sort(items, comp=lambda x, y: x > y):
    """冒泡排序"""
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items

def bubble_sort(items, comp=lambda x, y: x > y):
    """搅拌排序(冒泡排序升级版)"""
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items

def merge(items1, items2, comp=lambda x, y: x < y):
    """合并(将两个有序的列表合并成一个有序的列表)"""
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items

def merge_sort(items, comp=lambda x, y: x < y):
    # return _merge_sort(list(items), comp)
    return _merge_sort(items, comp)

def _merge_sort(items, comp):
    """归并排序"""
    if len(items) < 2:
        return items
    mid = len(items) // 2
    left = _merge_sort(items[:mid], comp)
    right = _merge_sort(items[mid:], comp)
    return merge(left, right, comp)


'''查找类'''
def seq_search(items, key):
    """顺序查找"""
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1

def bin_search(items, key):
    """折半查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1
'''
常用算法：

穷举法 - 又称为暴力破解法，对所有的可能性进行验证，直到找到正确答案。
贪婪法 - 在对问题求解时，总是做出在当前看来最好的选择，不追求最优解，快速找到满意解。
分治法 - 把一个复杂的问题分成两个或更多的相同或相似的子问题，再把子问题分成更小的子问题，直到可以直接求解的程度，最后将子问题的解进行合并得到原问题的解。
回溯法 - 回溯法又称为试探法，按选优条件向前搜索，当搜索到某一步发现原先选择并不优或达不到目标时，就退回一步重新选择。
动态规划 - 基本思想也是将待求解问题分解成若干个子问题，先求解并保存这些子问题的解，避免产生大量的重复运算。
'''
# 穷举法例子：百钱百鸡和五人分鱼。
# 公鸡5元一只 母鸡3元一只 小鸡1元三只
# 用100元买100只鸡 问公鸡/母鸡/小鸡各多少只
def qiongJu1():
    for x in range(20):
        for y in range(33):
            z = 100 - x - y
            if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
                print(x, y, z)

# A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
# 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
# B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
# 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼
def qiongJu2(): #真菜鸡，暂时看不太懂题目解法
    fish = 6
    while True:
        total = fish
        enough = True  #设置flag
        for _ in range(5):  #5个人
            if (total - 1) % 5 == 0:
                total = (total - 1) // 5 * 4
            else:
                enough = False
                break
        if enough:
            print(fish)
            break
        fish += 5

"""
贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
输入：
20 6
电脑 200 20
收音机 20 4
钟 175 10
花瓶 50 2
书 10 1
油画 90 9
"""
class Thing(object):
    """物品"""

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        """价格重量比"""
        return self.price / self.weight


def input_thing():
    """输入物品信息"""
    name_str, price_str, weight_str = input().split()
    return name_str, int(price_str), int(weight_str)


def tanLanMain():
    """主函数"""
    print('请输入问题：')
    max_weight, num_of_things = map(int, input().split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))
    all_things.sort(key=lambda x: x.value, reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print(f'小偷拿走了{thing.name}')
            total_weight += thing.weight
            total_price += thing.price
    print(f'总价值: {total_price}美元')

# 分治法例子：快速排序。
"""
快速排序 - 选择枢轴对元素进行划分，左边都比枢轴小右边都比枢轴大
"""
def quick_sort(items, comp=lambda x, y: x <= y):
    # items = list(items)[:]
    items = items[:]
    _quick_sort(items, 0, len(items) - 1, comp)
    return items


def _quick_sort(items, start, end, comp):
    if start < end:
        pos = _partition(items, start, end, comp)
        _quick_sort(items, start, pos - 1, comp)
        _quick_sort(items, pos + 1, end, comp)


def _partition(items, start, end, comp):
    pivot = items[end]
    i = start - 1
    for j in range(start, end):
        if comp(items[j], pivot):
            i += 1
            items[i], items[j] = items[j], items[i]
    items[i + 1], items[end] = items[end], items[i + 1]
    return i + 1

# 回溯法例子：骑士巡逻。
"""
递归回溯法：叫称为试探法，按选优条件向前搜索，当搜索到某一步，发现原先选择并不优或达不到目标时，
就退回一步重新选择，比较经典的问题包括骑士巡逻、八皇后和迷宫寻路等。
"""
import sys
import time

SIZE = 5
total = 0


def print_board(board):
    for row in board:
        for col in row:
            print(str(col).center(4), end='')
        print()


def patrol(board, row, col, step=1):
    if row >= 0 and row < SIZE and \
            col >= 0 and col < SIZE and \
            board[row][col] == 0:
        board[row][col] = step
        if step == SIZE * SIZE:
            global total
            total += 1
            print(f'第{total}种走法: ')
            print_board(board)
        patrol(board, row - 2, col - 1, step + 1)
        patrol(board, row - 1, col - 2, step + 1)
        patrol(board, row + 1, col - 2, step + 1)
        patrol(board, row + 2, col - 1, step + 1)
        patrol(board, row + 2, col + 1, step + 1)
        patrol(board, row + 1, col + 2, step + 1)
        patrol(board, row - 1, col + 2, step + 1)
        patrol(board, row - 2, col + 1, step + 1)
        board[row][col] = 0


def huiSuMain():
    board = [[0] * SIZE for _ in range(SIZE)]
    patrol(board, SIZE - 1, SIZE - 1)

# 动态规划例子：子列表元素之和的最大值。
'''
说明：子列表指的是列表中索引（下标）连续的元素构成的列表；列表中的元素是int类型，
可能包含正整数、0、负整数；程序输入列表中的元素，输出子列表元素求和的最大值，
例如：
输入：1 -2 3 5 -3 2
输出：8

输入：0 -2 3 5 -1 2
输出：9

输入：-9 -2 -3 -5 -3
输出：-2
'''
def dongTaiGuiHuaMain():
    # items = list(map(int, input().split()))
    items = [*map(int, input().split())] #对其进行列表解包
    overall = partial = items[0]
    for i in range(1, len(items)):
        partial = max(items[i], partial + items[i])
        overall = max(partial, overall)
    print(overall)
# 说明：上述题目最容易想到的解法是使用二重循环，但是代码的时间性能将会变得非常的糟糕。
# 使用动态规划的思想，仅仅是多用了两个变量，就将原来$O(N^2)$复杂度的问题变成了$O(N)$。

# 装饰器函数（使用装饰器和取消装饰器）
# 例子：输出函数执行时间的装饰器。
def record_time(func):
    """自定义装饰函数的装饰器"""
    from functools import wraps
    from time import time

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f'{func.__name__}: {time() - start}秒')
        return result

    return wrapper

#装饰器要这样之才能使用
@record_time
def record_time_test():
    pass

# 例子：用装饰器来实现单例模式。
def singleton(cls):
    """装饰类的装饰器"""
    from functools import wraps

    instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class President:
    """总统(单例类)"""
    pass


# 线程安全的单例装饰器。
def singleton(cls):
    """线程安全的单例装饰器"""
    from functools import wraps
    from threading import RLock

    instances = {}
    locker = RLock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            with locker:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper

# 面向对象相关知识
# 三大支柱：封装、继承、多态
# 例子：工资结算系统。
"""
月薪结算系统 - 部门经理每月15000 程序员每小时200 销售员1800底薪加销售额5%提成
"""
from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """员工(抽象类)"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """结算月薪(抽象方法)"""
        pass


class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """程序员"""

    def __init__(self, name, working_hour=0):
        self.working_hour = working_hour
        super().__init__(name)

    def get_salary(self):
        return 200.0 * self.working_hour


class Salesman(Employee):
    """销售员"""

    def __init__(self, name, sales=0.0):
        self.sales = sales
        super().__init__(name)

    def get_salary(self):
        return 1800.0 + self.sales * 0.05


class EmployeeFactory:
    """创建员工的工厂（工厂模式 - 通过工厂实现对象使用者和对象之间的解耦合）"""

    @staticmethod
    def create(emp_type, *args, **kwargs):
        """创建员工"""
        all_emp_types = {'M': Manager, 'P': Programmer, 'S': Salesman}
        cls = all_emp_types[emp_type.upper()]   #强制大写
        return cls(*args, **kwargs) if cls else None


def main1():
    """主函数"""
    emps = [
        EmployeeFactory.create('M', '曹操'),
        EmployeeFactory.create('P', '荀彧', 120),
        EmployeeFactory.create('P', '郭嘉', 85),
        EmployeeFactory.create('S', '典韦', 123000),
    ]
    for emp in emps:
        print(f'{emp.name}: {emp.get_salary():.2f}元')

# 类与类之间的关系

# is-a关系：继承
# has-a关系：关联 / 聚合 / 合成   就是部分与整体的关系，同生死，共命运（具有相同的生命周期）
# use-a关系：依赖    仅仅是使用关系，来帮忙的，没有相同的生命周期。大难临头各自飞的感觉
# 例子：扑克游戏。

"""
经验：符号常量总是优于字面常量，枚举类型是定义符号常量的最佳选择
"""
from enum import Enum, unique

import random


@unique
class Suite(Enum):
    """花色"""

    SPADE, HEART, CLUB, DIAMOND = range(4)

    def __lt__(self, other):
        return self.value < other.value


class Card():
    """牌"""

    def __init__(self, suite, face):
        """初始化方法"""
        self.suite = suite
        self.face = face

    def show(self):
        """显示牌面"""
        suites = ['♠︎', '♥︎', '♣︎', '♦︎']
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'

    def __repr__(self):
        return self.show()


class Poker():
    """扑克"""

    def __init__(self):
        self.index = 0
        self.cards = [Card(suite, face)
                      for suite in Suite
                      for face in range(1, 14)]

    def shuffle(self):
        """洗牌（随机乱序）"""
        random.shuffle(self.cards)
        self.index = 0

    def deal(self):
        """发牌"""
        card = self.cards[self.index]
        self.index += 1
        return card

    @property
    def has_more(self):
        return self.index < len(self.cards)


class Player():
    """玩家"""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        """摸一张牌"""
        self.cards.append(card)

    def sort(self, comp=lambda card: (card.suite, card.face)):
        """整理手上的牌"""
        self.cards.sort(key=comp)


def main2():
    """主函数"""
    #初始化扑克牌
    poker = Poker()
    #打乱一副全新的扑克牌
    poker.shuffle()
    #初始化玩家
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]

    while poker.has_more:   #还有牌量剩余就继续发牌
        for player in players:
            player.get_one(poker.deal())    #玩家得到一张发牌
    for player in players:
        player.sort()   #对玩家手牌进行排序
        print(player.name, end=': ')
        print(player.cards)

'''
面向对象设计原则:
单一职责原则 （SRP）- 一个类只做该做的事情（类的设计要高内聚）
开闭原则 （OCP）- 软件实体应该对扩展开发对修改关闭
依赖倒转原则（DIP）- 面向抽象编程（在弱类型语言中已经被弱化）
里氏替换原则（LSP） - 任何时候可以用子类对象替换掉父类对象
接口隔离原则（ISP）- 接口要小而专不要大而全（Python中没有接口的概念）
合成聚合复用原则（CARP） - 优先使用强关联关系而不是继承关系复用代码
最少知识原则（迪米特法则，LoD）- 不要给没有必然联系的对象发消息
说明：12457放在一起称为面向对象的SOLID原则。
'''

'''
GoF设计模式:
创建型模式：单例、工厂、建造者、原型
结构型模式：适配器、门面（外观）、代理
行为型模式：迭代器、观察者、状态、策略
'''

# 生成器是语法简化版的迭代器。
def fib(num):
    """生成器"""
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a

# 生成器进化为协程。->协程简单的说就是可以相互协作的子程序
def calc_avg():
    """流式计算平均值"""
    total, counter = 0, 0
    avg_value = None
    while True:
        value = yield avg_value
        total, counter = total + value, counter + 1
        avg_value = total / counter

'''
重点：多线程和多进程的比较。

以下情况需要使用多线程：
程序需要维护许多共享的状态（尤其是可变状态），Python中的列表、字典、集合都是线程安全的，所以使用线程而不是进程维护共享状态的代价相对较小。
程序会花费大量时间在I/O操作上，没有太多并行计算的需求且不需占用太多的内存。

以下情况需要使用多进程：
程序执行计算密集型任务（如：字节码操作、数据处理、科学计算）。
程序的输入可以并行的分成块，并且可以将运算结果合并。
程序在内存使用方面没有任何限制且不强依赖于I/O操作（如：读写文件、套接字等）。
'''

'''
异步处理：从调度程序的任务队列中挑选任务，该调度程序以交叉的形式执行这些任务，
我们并不能保证任务将以某种顺序去执行，因为执行顺序取决于队列中的一项任务是否愿意将CPU处理时间让位给另一项任务。
异步任务通常通过多任务协作处理的方式来实现，由于执行时间和顺序的不确定，
因此需要通过回调式编程或者future对象来获取任务执行的结果。
Python 3通过asyncio模块和await和async关键字（在Python 3.7中正式被列为关键字）来支持异步处理。
'''
"""
异步I/O - async / await
"""
import asyncio


def num_generator(m, n):
    """指定范围的数字生成器"""
    yield from range(m, n + 1)


async def prime_filter(m, n):
    """素数过滤器"""
    primes = []
    for i in num_generator(m, n):
        flag = True
        for j in range(2, int(i ** 0.5 + 1)):
            if i % j == 0:
                flag = False
                break
        if flag:
            print('Prime =>', i)
            primes.append(i)

        await asyncio.sleep(0.001)
    return tuple(primes)


async def square_mapper(m, n):
    """平方映射器"""
    squares = []
    for i in num_generator(m, n):
        print('Square =>', i * i)
        squares.append(i * i)

        await asyncio.sleep(0.001)
    return squares


def main3():
    """主函数"""
    loop = asyncio.get_event_loop()
    future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
    future.add_done_callback(lambda x: print(x.result()))
    loop.run_until_complete(future)
    loop.close()
# 说明：上面的代码使用get_event_loop函数获得系统默认的事件循环，
# 通过gather函数可以获得一个future对象，future对象的add_done_callback可以添加执行完成时的回调函数，
# loop对象的run_until_complete方法可以等待通过future对象获得协程执行结果。

# 异步的从5个URL中获取页面并通过正则表达式的命名捕获组提取了网站的标题。
import asyncio
import re

import aiohttp

PATTERN = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')


async def fetch_page(session, url):
    async with session.get(url, ssl=False) as resp:
        return await resp.text()


async def show_title(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch_page(session, url)
        print(PATTERN.search(html).group('title'))


def main4(): #异步获取网站标题
    urls = ('https://www.python.org/', # Welcome to Python.org
            'https://git-scm.com/',    # Git
            'https://www.jd.com/',     # 京东(JD.COM)-正品低价、品质保障、配送及时、轻松购物！
            'https://www.taobao.com/', # 淘宝网 - 淘！我喜欢
            'https://www.douban.com/') # 豆瓣
    loop = asyncio.get_event_loop()
    cos = [show_title(url) for url in urls]  # 异步输出就不是严格按照网站列表下标顺序输出了
    loop.run_until_complete(asyncio.wait(cos))
    loop.close()

'''
重点：异步I/O与多进程的比较。

当程序不需要真正的并发性或并行性，而是更多的依赖于异步处理和回调时，asyncio就是一种很好的选择。
如果程序中有大量的等待与休眠时，也应该考虑asyncio，它很适合编写没有实时数据处理需求的Web应用服务器。


Python还有很多用于处理并行任务的三方库，例如：joblib、PyMP等。
实际开发中，要提升系统的可扩展性和并发性通常有垂直扩展（增加单个节点的处理能力）和水平扩展（将单个节点变成多个节点）两种做法。
可以通过消息队列来实现应用程序的解耦合，消息队列相当于是多线程同步队列的扩展版本，不同机器上的应用程序相当于就是线程，
而共享的分布式消息队列就是原来程序中的Queue。消息队列（面向消息的中间件）的最流行和最标准化的实现是AMQP（高级消息队列协议），
AMQP源于金融行业，提供了排队、路由、可靠传输、安全等功能，最著名的实现包括：Apache的ActiveMQ、RabbitMQ等。


要实现任务的异步化，可以使用名为Celery的三方库。Celery是Python编写的分布式任务队列，
它使用分布式消息进行工作，可以基于RabbitMQ或Redis来作为后端的消息代理。
'''

if __name__ == '__main__':
    item1 = [34,342,234,2,5,46,32,53]
    item2 = [3,32,34,21,65,456,132,30]
    item3 = [-9 -2 -3 -5 -3]
    pass
    # main()
    # list()
    # heap()
    # itertool()
    # collection()
    # print(select_sort([34,342,234,2,5,46,32,53]))
    # print(_merge_sort(item1,comp= lambda x,y : x < y))
    # print(merge_sort(item2))
    # qiongJu1()
    # qiongJu2()
    # tanLanMain()
    # print(quick_sort(item2))
    # huiSuMain()
    # dongTaiGuiHuaMain()

    #filter()过滤函数，满足要求的通通不要
    items1 = [*map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10)))]
    items2 = [x ** 2 for x in range(1, 10) if x % 2]
    # print(items1)
    # print(items2)

    #装饰器 没搞懂
    # record_time_test()
    # President()
    #类的封装、继承和多态
    # main1()
    # 类与类之间的关系
    # main2()

    # yield返回的是迭代器
    # x = fib(5)
    # print(x)
    # print(type(x))
    # print([*x])

    # 生成器进化为协程。->协程简单的说就是可以相互协作的子程序
    # gen = calc_avg()
    # next(gen)
    # print(gen.send(10))
    # print(gen.send(20))
    # print(gen.send(30))

    # 还有多进程解决python GIL 全局锁问题  多进程  线程池详细看源代码

    # main3()
    main4()






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

if __name__ == '__main__':
    pass
    # main()
    # list()
    # heap()
    # itertool()
    collection()

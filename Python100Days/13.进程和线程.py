# coding=utf-8
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/9/13 11:08
# @Software: PyCharm

from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    #这里只能顺序执行，没有并发非常浪费时间
    start = time()
    download_task('Python从入门到住院.pdf')
    download_task('Peking Hot.avi')
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))

# Python中的多进程
def download_task1(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main1():
    start = time()
    #创建进程1
    p1 = Process(target=download_task1, args=('Python从入门到住院.pdf', ))
    p1.start()
    #创建进程2
    p2 = Process(target=download_task1, args=('Peking Hot.avi', ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))
'''
在上面的代码中，我们通过Process类创建了进程对象，通过target参数我们传入一个函数来表示进程启动后要执行的代码，
后面的args是一个元组，它代表了传递给函数的参数。Process对象的start方法用来启动进程，
而join方法表示等待进程执行结束。运行上面的代码可以明显发现两个下载任务“同时”启动了，
而且程序的执行时间将大大缩短，不再是两个任务的时间总和。下面是程序的一次执行结果。
'''

# Python中的多线程
from random import randint
from threading import Thread
from time import time, sleep


def download(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main2():
    start = time()
    t1 = Thread(target=download, args=('Python从入门到住院.pdf',))
    t1.start()
    t2 = Thread(target=download, args=('Peking Hot.avi',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.3f秒' % (end - start))

# 继承Thread类的方式来创建自定义的线程类，然后再创建线程对象并启动线程
class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成! 耗费了%d秒' % (self._filename, time_to_download))


def main3():
    start = time()
    t1 = DownloadTask('Python从入门到住院.pdf')
    t1.start()
    t2 = DownloadTask('Peking Hot.avi')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


# 100个线程分别向账户中转入1元钱
from time import sleep
from threading import Thread, Lock
class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 先获取锁才能执行后续的代码
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # 在finally中执行释放锁的操作保证正常异常锁都能释放
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)

def main4():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)


# 例子1：将耗时间的任务放到线程中以获得更好的用户体验。
# import time
# import tkinter
# import tkinter.messagebox
#
#
# def download5():
#     # 模拟下载任务需要花费10秒钟时间
#     time.sleep(10)
#     tkinter.messagebox.showinfo('提示', '下载完成!')
#
#
# def show_about():
#     tkinter.messagebox.showinfo('关于', '作者: 骆昊(v1.0)')
#
#
# def main5():
#     top = tkinter.Tk()
#     top.title('单线程')
#     top.geometry('200x150')
#     top.wm_attributes('-topmost', True)
#
#     panel = tkinter.Frame(top)
#     button1 = tkinter.Button(panel, text='下载', command=download5)
#     button1.pack(side='left')
#     button2 = tkinter.Button(panel, text='关于', command=show_about)
#     button2.pack(side='right')
#     panel.pack(side='bottom')
#
#     tkinter.mainloop()

#修改后
import time
import tkinter
import tkinter.messagebox
from threading import Thread


def main5():

    class DownloadTaskHandler(Thread):

        def run(self):
            time.sleep(10)
            tkinter.messagebox.showinfo('提示', '下载完成!')
            # 启用下载按钮
            button1.config(state=tkinter.NORMAL)

    def download():
        # 禁用下载按钮
        button1.config(state=tkinter.DISABLED)
        # 通过daemon参数将线程设置为守护线程(主程序退出就不再保留执行)
        # 在线程中处理耗时间的下载任务
        DownloadTaskHandler(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('关于', '作者: 骆昊(v1.0)')

    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', 1)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()

# 例子2：使用多进程对复杂任务进行“分而治之”。
# 完成1~100000000求和的计算密集型任务
from multiprocessing import Process, Queue
from random import randint
from time import time


def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)


def main6():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    # 启动8个进程将数据切片后进行运算
    for _ in range(8):
        p = Process(target=task_handler,
                    args=(number_list[index:index + 12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    # 开始记录所有进程执行完成花费的时间--只计算进程执行的时间
    start = time()
    for p in processes:
        p.join()
    # 合并执行结果
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Execution time: ', (end - start), 's', sep='')


if __name__ == '__main__':
    # main()
    # main1()
    # main2()
    # main3()
    # main4()
    # main5()
    main6()

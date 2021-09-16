# coding=utf-8
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/9/12 18:37
# @Software: PyCharm


# GUI是图形用户界面的缩写，图形化的用户界面对使用过计算机的人来说应该都不陌生，在此也无需进行赘述。
# Python默认的GUI开发模块是tkinter（在Python 3以前的版本中名为Tkinter），从这个名字就可以看出它是基于Tk的，
# Tk是一个工具包，最初是为Tcl设计的，后来被移植到很多其他的脚本语言中，它提供了跨平台的GUI控件。
# 当然Tk并不是最新和最好的选择，也没有功能特别强大的GUI控件，事实上，开发GUI应用并不是Python最擅长的工作，
# 如果真的需要使用Python开发GUI应用，wxPython、PyQt、PyGTK等模块都是不错的选择。


# 使用Pygame进行游戏开发

# 制作游戏窗口
import pygame


def main():
    # # 初始化导入的pygame中的模块
    # pygame.init()
    # # 初始化用于显示的窗口并设置窗口尺寸
    # screen = pygame.display.set_mode((800, 600))
    # # 设置当前窗口的标题
    # pygame.display.set_caption('大球吃小球')
    # running = True
    # # 开启一个事件循环处理发生的事件
    # while running:
    #     # 从消息队列中获取事件并对事件进行处理
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False


    # 在窗口中绘图
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    # 设置窗口的背景色(颜色是由红绿蓝三原色构成的元组)
    screen.fill((242, 242, 242))
    # 绘制一个圆(参数分别是: 屏幕, 颜色, 圆心位置, 半径, 0表示填充圆)
    pygame.draw.circle(screen, (255, 0, 0,), (100, 100), 30, 0)
    # 刷新当前窗口(渲染窗口将绘制的图像呈现出来)
    pygame.display.flip()
    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()



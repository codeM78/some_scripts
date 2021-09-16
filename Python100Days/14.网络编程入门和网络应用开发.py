# coding=utf-8
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/9/13 13:54
# @Software: PyCharm

# 实现了一个提供时间日期的服务器。
from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime


# def main():
#     # 1.创建套接字对象并指定使用哪种传输服务
#     # family=AF_INET - IPv4地址
#     # family=AF_INET6 - IPv6地址
#     # type=SOCK_STREAM - TCP套接字
#     # type=SOCK_DGRAM - UDP套接字
#     # type=SOCK_RAW - 原始套接字
#     server = socket(family=AF_INET, type=SOCK_STREAM)
#     # 2.绑定IP地址和端口(端口用于区分不同的服务)
#     # 同一时间在同一个端口上只能绑定一个服务否则报错
#     server.bind(('192.168.31.116', 6789))
#     # 3.开启监听 - 监听客户端连接到服务器
#     # 参数512可以理解为连接队列的大小
#     server.listen(512)
#     print('服务器启动开始监听...')
#     while True:
#         # 4.通过循环接收客户端的连接并作出相应的处理(提供服务)
#         # accept方法是一个阻塞方法如果没有客户端连接到服务器代码不会向下执行
#         # accept方法返回一个元组其中的第一个元素是客户端对象
#         # 第二个元素是连接到服务器的客户端的地址(由IP和端口两部分构成)
#         client, addr = server.accept()
#         print(str(addr) + '连接到了服务器.')
#         # 5.发送数据
#         client.send(str(datetime.now()).encode('utf-8'))
#         # 6.断开连接
#         client.close()

# 使用多线程技术处理多个用户请求的服务器
from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread


def main():

    # 自定义线程类
    class FileTransferHandler(Thread):

        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'guido.jpg'
            # JSON是纯文本不能携带二进制数据
            # 所以图片的二进制数据要处理成base64编码
            my_dict['filedata'] = data
            # 通过dumps函数将字典处理成JSON字符串
            json_str = dumps(my_dict)
            # 发送JSON字符串
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    # 1.创建套接字对象并指定使用哪种传输服务
    server = socket()
    # 2.绑定IP地址和端口(区分不同的服务)
    server.bind(('192.168.31.116', 5566))
    # 3.开启监听 - 监听客户端连接到服务器
    server.listen(512)
    print('服务器启动开始监听...')
    with open('guido.jpg', 'rb') as f:
        # 将二进制数据处理成base64再解码成字符串
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        # 启动一个线程来处理客户端的请求
        FileTransferHandler(client).start()


if __name__ == '__main__':
    main()

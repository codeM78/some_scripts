# coding=utf-8
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/8/31 12:39
# @Software: PyCharm

# 查看matplotlib配置文件路径
# import matplotlib
# path = matplotlib.matplotlib_fname()
# print(path)

import matplotlib.pyplot as plt
import random
# # 解决中文乱码--已经在配置文件里彻底解决了，就不用每次都加载这两个语句了
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

x = range(60)
y = [random.uniform(15,18) for i in x]

plt.figure(figsize=(20,10),dpi=80)
plt.plot(x,y)
#设置x轴意义
x_lable = [f"11点{i}分" for i in x]
#设置x轴刻度
plt.xticks(x[::5],x_lable[::5])
#设置y轴刻度
plt.yticks(range(0,40,5))

#显示图像
plt.show()


#1.准备数据
x = range(60)
y_shanghai = [random.uniform(15,18) for i in x]
y_beijing = [random.uniform(5,8) for i in x]

# 2.创建画布
# plt.figure(figsize=(20,8), dpi=80)
figure, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8), dpi=80)

# 3.绘制图像
axes[0].plot(x,y_shanghai, color='r', linestyle='--', label='上海')
axes[1].plot(x,y_beijing, color='b', label='北京')

# 修改x，y的刻度
# x轴的刻度说明
x_lable = [f'11点{i}分' for i in x]
axes[0].set_xticks(x[::10])
axes[0].set_xticklabels(x_lable[::10])
axes[0].set_yticks(range(0, 40, 5))

axes[1].set_xticks(x[::10])
axes[1].set_xticklabels(x_lable[::10])
axes[1].set_yticks(range(0, 40, 5))

# 添加网格显示
# plt.grid(True, linestyle='--', alpha=0.5)
axes[0].grid(linestyle='--', alpha=0.5)
axes[1].grid(linestyle='--', alpha=0.5)


# 添加描述信息
axes[0].set_xlabel('时间变化')
axes[0].set_ylabel('温度变化')
axes[0].set_title('上海11点到12点每分钟的温度变化状况')
axes[1].set_xlabel('时间变化')
axes[1].set_ylabel('温度变化')
axes[1].set_title('北京11点到12点每分钟的温度变化状况')

# 显示图例
# plt.legend()
axes[0].legend()
axes[1].legend()

# 4.显示图像
plt.show()



# import random
# import matplotlib.pyplot as plt
# #1.准备数据
# x = range(60)
# y = [random.uniform(15,18) for i in x]
#
#
# # 解决中文乱码--已经在配置文件里彻底解决了，就不用每次都加载这两个语句了
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.rcParams['axes.unicode_minus']=False
#
# # 2.创建画布
# plt.figure(figsize=(20,8), dpi=80)
# # 3.绘制图像
# plt.plot(x,y)
#
# # 修改x，y的刻度
# # x轴的刻度说明
# x_lable = [f'11h{i}m' for i in x]
# plt.xticks(x[::5],x_lable[::5])
# plt.yticks(range(0, 40, 5))
#
# # 4.显示图像
# plt.show()





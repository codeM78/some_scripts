# codeing : utf-8
# 学习单位  : 郑州大学
# @Author  : 铭同学
# @Time    : 2021/8/23 9:55
# @Software: PyCharm
import json
from pyecharts import options as opts
from pyecharts.charts import TreeMap

'''利用python库绘制treemap可视化页面'''
#代码没有任何问题就是数据格式有误，参照disk.tree.json的数据可是就能完美可视化


# with open('data/disk.tree.json', 'r',encoding='utf-8') as f:
# with open('data/data1.json', 'r',encoding='utf-8') as f:
with open('data/demo-test_level4.json', 'r', encoding='utf-8') as f:
# with open('data/demo-test-En.json', 'r',encoding='utf-8') as f:
    data = json.load(f)
c = (
    TreeMap()   #实例化树图
        .add(series_name='Zhengzhou',
            data=data,  #读取文本中的数据
             levels=[
                 opts.TreeMapLevelsOpts(
                     treemap_itemstyle_opts=opts.TreeMapItemStyleOpts(
                         border_color='#555', border_width=4, gap_width=4
                     )
                 ),
                 opts.TreeMapLevelsOpts(
                     color_saturation=[0.3,0.6],
                     treemap_itemstyle_opts=opts.TreeMapItemStyleOpts(
                         border_color_saturation=0.7, gap_width=2, border_width=5
                     ),
                 ),
                 opts.TreeMapLevelsOpts(
                     color_saturation=[0.3,0.5],
                     treemap_itemstyle_opts=opts.TreeMapItemStyleOpts(
                         border_color_saturation=0.6, gap_width=1
                     ),
                 ),
                 opts.TreeMapLevelsOpts(color_saturation=[0.3,0.5]),

             ],
             )
    .set_global_opts(title_opts=opts.TitleOpts(title='TreeMap-Levels-setting'))
    .render('templates/demo-test.html')
)

#! /usr/bin/python
# -*- coding: UTF-8 -*-

import numpy
import matplotlib.pyplot as plt

# x为横坐标，y为纵坐标
x = numpy.array([1,2,3,4,5,6,7,8])
y = numpy.array([3,5,7,6,2,6,10,15])

# plot：折线图
plt.plot(x,y,'r')
plt.plot(x,y,"g",lw=10) #lw为粗度line weight

# bar：柱状图
plt.bar(x,y)

# pie：饼状图

# labels为饼图的各个项，percent为各项的比例
labels = 'a', 'b', 'c', 'd'
percent = [10,20,30,40]

# shadow为阴影，autopct为显示的数据，2f为两位浮点数
plt.pie(x=percent, labels=labels, shadow=True, autopct="%1.2f%%")

plt.show()


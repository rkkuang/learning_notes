总结自 https://github.com/rkkuang/aeroastro/blob/master/clean/codes_v2/utils.py

1. imshow 显示图像，坐标轴刻度单位不想用像素，并用科学计数法表示，可以：

from matplotlib.ticker import ScalarFormatter
plt.imshow(whichimg, cmap = plt.cm.jet,  origin='lower',extent=extent )#cmap = plt.cm.gray_r
其中extend = (xmin,xmax,ymin,ymax)为新的坐标范围

用科学计数法表示:
ax = plt.gca()
xfmt = ScalarFormatter(useMathText=True)
xfmt.set_powerlimits((0, 0))  # Or whatever your limits are . . .
ax.yaxis.set_major_formatter(xfmt)
ax.xaxis.set_major_formatter(xfmt)


2.
用科学计数法之后，那个 x10^2 与 title 重叠，可以将title位置设置的高一点：
plt.title(title, y=1.05)

3. colorbar 刻度设置，标注设置：

cbar = plt.colorbar()
cbar.set_label(r'Flux $(J_y)$')
cbar.formatter.set_powerlimits((0, 0))
cbar.update_ticks()

4. subplot画完图弹出的窗口里，图重叠到一块了，可以将窗口全屏，然后设置为 tight_layout

5. python matplotlib chinese

https://www.jb51.net/article/115533.htm
5.1. 下载中文字体simhei.ttf, 网址为http://fontzone.net/download/simhei
5.2. 搜索 matplotlib 字体的安装位置
$locate -b '\mpl-data'
会得到 这个路径/usr/share/matplotlib/mpl-data下面有fonts/ttf这个目录，进入这个目录，把刚才下载的simhei.ttf 字体复制到这个目录下，注意权限和归属是否与其它字体一致，我的是归于root用户的，所以用root 用户复制过来。
5.3. 删除当前用户matplotlib 的缓冲文件（如果没有直接进入第四步）
$cd ~/.cache/matplotlib
$rm -rf *.*
5.4.代码中调整字体
#!/usr/bin/env python
#coding:utf-8
"""a demo of matplotlib"""
import matplotlib as mpl
from matplotlib import pyplot as plt
mpl.rcParams[u'font.sans-serif'] = ['simhei']
mpl.rcParams['axes.unicode_minus'] = False
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
#创建一副线图,x轴是年份,y轴是gdp
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
#添加一个标题
plt.title(u'名义GDP')
#给y轴加标记
plt.ylabel(u'十亿美元')
plt.show()
其中#coding:utf-8 说明文件编码格式
mpl.rcParams[u'font.sans-serif'] = ['simhei'] 用simhei 字体显示中文
mpl.rcParams['axes.unicode_minus'] = False 这个用来正常显示负号
plt.title(u'名义GDP')这里的u 最好不要少
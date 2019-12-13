总结自 https://github.com/rkkuang/aeroastro/blob/master/clean/codes_v2/utils.py

==========================================
https://www.zhihu.com/question/21953954
python如何调整子图的大小？

grid = plt.GridSpec(2, 3, wspace=0.5, hspace=0.5)
plt.subplot(grid[0,0])
plt.subplot(grid[0,1:3])
plt.subplot(grid[1,0:2])
plt.subplot(grid[1,2])
==========================================
python 调整colorbar 大小
srcplaneim = plt.imshow(XXXimg)
add_colorbar(srcplaneim)

from mpl_toolkits import axes_grid1
def add_colorbar(im, aspect=20, pad_fraction=0.5, **kwargs):
    """Add a vertical color bar to an image plot."""
    divider = axes_grid1.make_axes_locatable(im.axes)
    width = axes_grid1.axes_size.AxesY(im.axes, aspect=1./aspect)
    pad = axes_grid1.axes_size.Fraction(pad_fraction, width)
    current_ax = plt.gca()
    cax = divider.append_axes("right", size=width, pad=pad)
    plt.sca(current_ax)
    return im.axes.figure.colorbar(im, cax=cax, **kwargs)




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








plt.imshow(confusion_matrix_percent,cmap='gray')
plt.colorbar()

 plt.show()
 在上面的代码中，设置cmap=‘gray’，表示绘制灰度图，若需要绘制彩色图，可设置其它值,个人比较喜欢用 PRGn或者PRGn_r



 cmap的候选值有

 'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Vega10', 'Vega10_r', 'Vega20', 'Vega20_r', 'Vega20b', 'Vega20b_r', 'Vega20c', 'Vega20c_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spectral', 'spectral_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'viridis', 'viridis_r', 'winter', 'winter_r'

high contrast colormap
    #https://stackoverflow.com/questions/53101815/improve-color-contrast-in-matplotlib
        # try one of the continuous colormaps, like viridis or gist_ncar. If you don't need all colors to be different, try one of the repeating maps like flag or prism



https://stackoverflow.com/questions/36437584/how-to-set-xticks-and-yticks-with-my-imshow-plot
You are missing the extent argument in imshow. imshow assumes that there is a linear relation between pixels and your "physical" unit. You could just use:

plt.imshow(a11, cmap='hot', interpolation='nearest', extent=[0,88,0,8], origin='lower')
The extent variable has to be given such that extent=[xmin,xmax,ymin,ymax]. The origin='lower' argument is to specify that your [0,0] coordinate has to be placed in the bottom left of the axis. Otherwise, it is placed in the top left of the axis.

Finally, for showing only some particular ticks, you may want to use:

ax = plt.gca()
xticks = [0,8,16,24,32,40,48,56,64,72,80,88]
yticks = [0,2,4,6,8]
ax.xaxis.set_xticks(xticks)
ax.xaxis.set_yticks(yticks)





https://littleround.cn/2019/01/04/Python%E5%88%B6%E4%BD%9C%E5%8A%A8%E6%80%81%E5%9B%BE-matplotlib.animation/
python animation

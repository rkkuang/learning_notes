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


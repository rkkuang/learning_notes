# https://pythonspot.com/3d-scatterplot/
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# Create data
N = 60


# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)#, axisbg="1.0"
ax = fig.gca(projection='3d')

n=0

plt.ion()    # 打开交互模式
for n in range(5):
    # ax.cla()   # Clear axis
    # plt.clf()   #
    # plt.cla()
    plt.cla()#去掉前面画下的红线
    
    g1 = (0.6 + 0.6 * np.random.rand(N), np.random.rand(N),0.4+0.1*np.random.rand(N))
    g2 = (0.4+0.3 * np.random.rand(N), 0.5*np.random.rand(N),0.1*np.random.rand(N))
    g3 = (0.3*np.random.rand(N),0.3*np.random.rand(N),0.3*np.random.rand(N))
    data = (g1, g2, g3)
    colors = ("red", "green", "blue")
    groups = ("coffee", "tea", "water")
    for data, color, group in zip(data, colors, groups):
        x, y, z = data
        ax.scatter(x, y, z, alpha=0.8, c=color, edgecolors='none', s=30, label=group)

    plt.draw()
    plt.pause(0.5)
    # plt.legend(loc=2)
# plt.title('Matplot 3d scatter plot')
    # ax.clear() # to clear the whole axes
    # plt.cla()

plt.ioff()
plt.show()
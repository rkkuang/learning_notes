# https://pythonspot.com/3d-scatterplot/
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

G = 

particleN = 60
class partical():
    def __init__(self, mass, pos, vel, acc, radius = 2.5):
        self.mass = mass
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.radius = radius
    def acceleration(self, other):
        # r = 
        pass



# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax = fig.gca(projection='3d')

n=0

plt.ion() # 打开交互模式
for n in range(5):
    plt.cla()#
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
plt.ioff()
plt.show()
import time
import random
# import ttk
# from tkinter import ttk
# # import tkMessageBox 
# from tkinter import messagebox

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


# from simulation import Space
# from simulation import ParticleEntryBox
import Space
import ParticleEntryBox
from tkinter import *

WIDTH = 640
HEIGHT= 480

class MainUserInterface:
    
    def __init__(self, master=None):
        ''' Main user interface for the application with the following master-slave relationship:
            
            master
                panedwindow
                    canvas
                    sidebar
                        random button
        '''

        # master.title("Gravitationally")
        # master.resizable(False, False)

        # create empty space attribute
        self.space = Space.Space() 

        # config master and panedwindow
        # self.master = master
        # self.panedwindow = ttk.Panedwindow(master, orient = HORIZONTAL)
        # self.panedwindow.pack(fill = BOTH, expand = True)

        # config sidebar and canvas
        # self.canvas = Canvas(self.panedwindow, width = 800, height = 640, background = 'black')
        # self.canvas = Canvas(self.panedwindow, width = WIDTH, height = HEIGHT, background = 'black')
        # self.sidebar = ttk.Frame(self.panedwindow, width = 150, height = 300)
        # self.panedwindow.add(self.sidebar)
        # self.panedwindow.add(self.canvas)

        # # config mouse button press on canvas
        # self.canvas.bind('<ButtonPress>', self.canvasPress)

        # # config random button
        # ttk.Button(self.sidebar, text = 'Random', command = self.runRandomSimulation).grid(row = 1, column = 0, padx = 3, pady = 3) 
        # ttk.Button(self.sidebar, text = 'Clear', command = self.clear).grid(row = 10, column = 0, padx = 3, pady = 3) 
        # ttk.Button(self.sidebar, text = 'ResetPos', command = self.resetaxes).grid(row = 20, column = 0, padx = 3, pady = 3) 

    def resetaxes(self):
        maxd = 0
        dx = 0
        dy = 0
        for particle in self.space.getParticles():
            if particle.d > maxd:
                maxd = particle.d
                dx = particle.r.x
                dy = particle.r.y
        for particle in self.space.getParticles():
            particle.r.x = particle.r.x - dx + WIDTH/2
            particle.r.y = particle.r.y - dy + HEIGHT/2
    
        
    def runSimulation(self,ax):
        ''' clear canvas and run simulation
        '''
        # self.canvas.delete('all')
        plt.cla()#

        # animation loop
        while True:
        # for nn in range(5):
            self.space.evolve()
            # self.canvas.delete('all')     
            plt.cla()#

            xyzlim = 100
            for particle in self.space.getParticles():
                # self.canvas.create_oval(particle.r.x, particle.r.y, particle.r.x + particle.d, particle.r.y + particle.d, fill = 'yellow')
                ax.scatter(particle.r.x, particle.r.y,particle.r.z,s=2*particle.d,c="r")
            # ax.set_xlim(-100,100)
            # ax.set_ylim(-100,100)
            # ax.set_zlim(-100,100)
            if abs(particle.r.x) >= xyzlim or abs(particle.r.y) >= xyzlim or abs(particle.r.z) >= xyzlim:
                xyzlim += 100
            ax.set_xlim(-xyzlim,xyzlim)
            ax.set_ylim(-xyzlim,xyzlim)
            ax.set_zlim(-xyzlim,xyzlim)
            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_zticks([])

            # plt.axis('off')
            plt.grid(b=None)

            plt.draw()
            plt.pause(0.0001)
            # self.canvas.update()
        
    def canvasPress(self, event):
        ''' Create popup entry box to add new particle onto canvas
        '''
        popup = ParticleEntryBox.ParticleEntryBox(self.master, self, event)
        self.master.wait_window(popup.textPrompt)
        self.runSimulation()

    def runRandomSimulation(self,ax):
        ''' run random simulation of n particles
        '''
        self.space.clearSpace()
        xyzpos = 60
        xyzvel = 10

        n = 200
        for i in range(n):
            m = random.uniform(100, 250)
            d = 10/m**(1/3)
            rx = random.uniform(-40, 40) 
            ry = random.uniform(-40, 40) 
            rz = random.uniform(-40, 40) 
            vx = random.uniform(-15, 15) 
            vy = random.uniform(-15, 15)
            vz = random.uniform(-15, 15)
            r = Space.Vector(rx, ry, rz)
            v = Space.Vector(vx, vy, vz)
            particle = Space.Particle(r, v, m, d)
            self.space.addParticle(particle)

        # n = 100
        # # use r, theta, phi
        # theta = 0
        # phirange = 90 # degree
        # particle = Space.Particle(Space.Vector(0, 0, 0), Space.Vector(0, 0, 0), 250000, 10/2500**(1/3))
        # self.space.addParticle(particle) 
        # for i in range(n):
        #     m = random.uniform(100, 250)
            
        #     r = random.uniform(0, xyzpos)
            
        #     # m = 10/r
        #     m /= (r/xyzpos)
        #     d = 10/m**(1/3)

        #     v = random.uniform(0, xyzvel)

        #     phi = random.uniform(0, phirange) 
        #     rx = r*np.cos(np.deg2rad(theta))*np.cos(np.deg2rad(phi))
        #     ry = r*np.cos(np.deg2rad(theta))*np.sin(np.deg2rad(phi))
        #     rz = r*np.sin(np.deg2rad(theta))
        #     vx = r**0.5*v*np.cos(np.deg2rad(90+phi))
        #     vy = r**0.5*v*np.sin(np.deg2rad(90+phi))
        #     vz = 0
        #     r = Space.Vector(rx, ry, rz)
        #     v = Space.Vector(vx, vy, vz)
        #     particle = Space.Particle(r, v, m, d)
        #     self.space.addParticle(particle)
        # for i in range(n):
        #     m = random.uniform(100, 250)
        #     d = 10/m**(1/3)
        #     r = random.uniform(0,xyzpos) 
        #     v = random.uniform(0, xyzvel)
        #     phi = random.uniform(180+0, 180+phirange) 
        #     rx = r*np.cos(np.deg2rad(theta))*np.cos(np.deg2rad(phi))
        #     ry = r*np.cos(np.deg2rad(theta))*np.sin(np.deg2rad(phi))
        #     rz = -r*np.sin(np.deg2rad(theta))
        #     vx = r**0.5*v*np.cos(np.deg2rad(90+phi))
        #     vy = r**0.5*v*np.sin(np.deg2rad(90+phi))
        #     vz = 0
        #     r = Space.Vector(rx, ry, rz)
        #     v = Space.Vector(vx, vy, vz)
        #     particle = Space.Particle(r, v, m, d)
        #     self.space.addParticle(particle)        
        

  

        self.runSimulation(ax)

    def clear(self):
        self.space.clearSpace()
        self.runSimulation()


def main():
    # root = Tk()
    # MainUserInterface(root)
    # mainloop()
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax = fig.gca(projection='3d')
    # plt.title("N body simulation, evolution of the universe")
    plt.suptitle("N body simulation\nevolution of the universe",size=20)

    # ax.set_xlim(-10,10)
    # ax.set_ylim(-10,10)
    # ax.set_zlim(-10,10)
    plt.ion() # 打开交互模式
    maininter = MainUserInterface()
    maininter.runRandomSimulation(ax)
    plt.ioff()



    plt.show()



if __name__ == '__main__': 
    main()
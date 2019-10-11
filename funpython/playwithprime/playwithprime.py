#https://www.youtube.com/watch?v=EK32jo7i5LQ
#Why do prime numbers make these spirals?

def isprime(x):
    for i in range(2, int(x**0.5+1)):
        if x%i == 0:
            return False
    return True

if __name__ == '__main__':
    # for i in range(2, 100):
    #     if isprime(i):
    #         print(i)

    import matplotlib.pylab as plt
    import numpy as np

    maxN = 3*10**4

    plt.figure()#figsize=(500,500)
    x = []
    y = []
    for i in range(2, maxN):
        if isprime(i):
            x.append(i*np.cos(i))
            y.append(i*np.sin(i))

    plt.scatter(x,y,s=1,c="b")
    #https://stackoverflow.com/questions/17990845/how-to-equalize-the-scales-of-x-axis-and-y-axis-in-python-matplotlib
    # plt.xlim(-maxN, maxN)
    # plt.ylim(-maxN, maxN)
    # plt.axis('equal')
    plt.xlabel(r"$r\cos\theta$")
    plt.ylabel(r"$r\sin\theta$")
    plt.title(r"Distribution of (r,$\theta$) with $r=\theta$ is prime number")
    plt.axis('square')
    plt.show()
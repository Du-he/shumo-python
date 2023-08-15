#用matplotlib制作动画

import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
fig,ax=plt.subplots()
x=np.arange(0,2*np.pi,0.01)
line,=ax.plot(x,np.sin(x))
def animate(i):
    line.set_ydata(np.sin(x+i/1000))
    return line,
def init():
    line.set_ydata(np.sin(x))
    return line,
ani=animation.FuncAnimation(fig=fig,func=animate,init_func=init,frames=1000,interval=10,blit=False)
plt.show(plt.show(block=True))
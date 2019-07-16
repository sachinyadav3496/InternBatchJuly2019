import matplotlib.pyplot as plt
from psutil import cpu_percent as cpu 
from time import sleep
from matplotlib.animation import FuncAnimation
plt.rcParams['animation.html'] = 'jshtml'
#%matplotlib notebook
x = list(range(1,51))
y = []
for var in range(50): 
    y.append(cpu())
    sleep(.2)  
fig,ax = plt.subplots()
ax.plot(x,y,'ro--')
def change(interval):
    x.pop(0)
    y.pop(0)
    x.append(x[-1]+1)
    y.append(cpu())
    ax.clear()
    ax.plot(x,y,'ro--')
    sleep(.5)
ani = FuncAnimation(fig,change,2000)
plt.show()
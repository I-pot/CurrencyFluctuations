#===================================================
#This is taken from below:
#https://medium.com/@gerald.hoxha94/partial-differential-equations-in-python-23ccd160c082
#===================================================
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import seaborn as sns
sns.set()

T = 100
u = np.zeros((100,100))
u[50,50] = 1

fig, ax = plt.subplots(figsize=(20,10))
ax.axis('off')
plot = ax.contourf(u, cmap='jet')
def ans(f):
    global u, plot
    
    #Time is not defined as the animation will do the loop for T times.
    for j in range(99):
        for i in range(1,99):
            u[i,j] += (u[i+1,j] + u[i,j+1] + u[i-1,j] + u[i,j-1] - 4*u[i,j])/4
    for c in plot.collections:
        c.remove()
    plot = ax.contourf(u, cmap='jet')
    return plot

anim = animation.FuncAnimation(fig, ans, frames=T)
plt.show()
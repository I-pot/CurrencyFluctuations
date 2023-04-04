#==============================================
#Testing some histogram stuff
#Topi Loytainen (2022)
#==============================================
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Fixing random state for reproducibility
np.random.seed(19680801)
# Fixing bin edges
HIST_BINS = np.linspace(-4, 4, 100) #len(HIST_BINS)=100
#[-4.         -3.91919192 ... 3.91919192  4.        ]

# histogram our data with numpy
data = np.random.randn(1000)
#[ 1.04930431e+00  8.66099175e-01 ... -3.37900358e-01  1.10828635e-01]
n, _ = np.histogram(data, HIST_BINS) #len(n) = 99

def prepare_animation(bar_container):

    def animate(frame_number):
        # simulate new data coming in
        data = np.random.randn(1000)
        n, _ = np.histogram(data, HIST_BINS)
        for count, rect in zip(n, bar_container.patches):
            rect.set_height(count)
        return bar_container.patches
    return animate

fig, ax = plt.subplots()
_, _, bar_container = ax.hist(data, HIST_BINS, lw=1, ec="yellow", fc="green", alpha=0.5) #The underscores work as a throwaway variable 
#i.e. hist returns tuple[list[float], list[float], BarContainer | list] from which we discard the two first ones: list[float], list[float]
ax.set_ylim(top=55)  # set safe limit to ensure that all data is visible.

ani = animation.FuncAnimation(fig, prepare_animation(bar_container), frames=50, interval=1000, repeat=False, blit=True)
plt.show()
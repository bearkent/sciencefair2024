import numpy as np
import matplotlib.pyplot as plt 

xs = np.linspace(0,1,10)
ys=(0,1,2,3,4,5,4,3,2,1)

p = np.polyfit(xs,ys,4)
t=np.linspace(0,1,50)

plt.plot(xs,ys,'o',t,p(t),'-')
plt.show()
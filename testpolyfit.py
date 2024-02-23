import numpy as np
import matplotlib.pyplot as plt 

xs = np.linspace(0,1,10)
ys=np.array([0,1,2,3,4,5,4,3,2,1])

p = np.polyfit(xs,ys,4)
t=np.linspace(0,1,50)

print(p)

# plt.plot(t,p(t))
# plt.show()
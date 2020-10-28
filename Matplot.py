import matplotlib.pyplot as plt
import  numpy as np

xpoints = np.array([1,2,6,8])
ypoints = np.array([3,8,1,10])

plt.plot(xpoints, ypoints)
#The plot() function is used to draw points (markers) in a diagram.
#By default, the plot() function draws a line from point to point.
plt.show()

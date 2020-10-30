import matplotlib.pyplot as plt
import  numpy as np

xpoints = np.array([1,2,6,8])
x1 = np.array([7,5,3,9,2])
ypoints = np.array([3,8,1,10])
y1 = np.array([6,9,5,8,4])
plt.plot(xpoints, ypoints,x1, y1,  'o:r')
#The plot() function is used to draw points (markers) in a diagram.
#By default, the plot() function draws a line from point to point.
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170,10,250)
plt.hist(x)#The hist() function will read the array and produce a histogram:
plt.show()
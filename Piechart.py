import matplotlib.pyplot as plt
import numpy as np

y = np.array([35,25,25,10,15])
mylabels = ["one","two","three","four","five"]

myexplode = [0.2,0,0,0,0.3]

plt.pie(y , labels=mylabels , startangle=90, explode=myexplode, shadow = True )
plt.legend()
plt.show()
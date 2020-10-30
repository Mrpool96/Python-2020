import matplotlib.pyplot as plt
import numpy as np

y = np.array([35,25,25,10,15])
mylabels = ["one","two","three","four","five"]

plt.pie(y , labels=mylabels)
plt.show()
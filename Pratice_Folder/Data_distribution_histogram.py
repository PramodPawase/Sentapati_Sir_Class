import numpy as np
import matplotlib.pyplot as plt

x=np.random.uniform(0.0,0.5,250)
print(plt.hist(x,5))
plt.show()


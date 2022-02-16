import numpy as np
import matplotlib.pyplot as plt
x=np.average(-10, 10, 0.01)
plt.plot(x, (x*x-x-6))
plt.show()

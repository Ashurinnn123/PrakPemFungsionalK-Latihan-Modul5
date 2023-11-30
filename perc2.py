import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([10, 8, 6])
ypoints = np.array([3, 10, 5])

plt.figure(figsize=(5,5))
plt.plot(xpoints, ypoints, color='blue')
plt.grid(True)
plt.xlim([0, 15])
plt.ylim([0, 15])
plt.show()

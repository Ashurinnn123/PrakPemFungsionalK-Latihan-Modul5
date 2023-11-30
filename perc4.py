import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [3, 7, 2, 8, 5]

plt.scatter(x, y, color='blue', marker='o', label='Data Points')
plt.title('Scatter Plot Data Points')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.legend()
plt.grid(True)
plt.show()
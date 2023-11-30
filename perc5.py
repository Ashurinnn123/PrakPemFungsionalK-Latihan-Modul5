import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm 

# Generate random data
sample = np.random.normal(loc=50, scale=5, size=1000)

# Calculate sample mean and standard deviation
sample_mean = np.mean(sample)
sample_std = np.std(sample)
print(f'Mean={sample_mean:.3f}\nStandard Deviation={sample_std:.3f}')

# Plot histogram
plt.hist(sample, bins=10, density=True, alpha=0.7, label='Sample Histogram')

# Fit a normal distribution to the data
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, sample_mean, sample_std)
plt.plot(x, p, 'k', linewidth=2, label='Fitted Normal Distribution')

# Add labels and legend
plt.xlabel('Values')
plt.ylabel('Probability Density')
plt.legend()

# Show the plot
plt.show()

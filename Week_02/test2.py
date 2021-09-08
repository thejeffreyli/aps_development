import matplotlib.pylab as plt
import numpy as np

# Create fake data
B = np.random.uniform(0, 10, size=(100, 100))


plt.contourf(B, vmin=0, vmax=3)
plt.colorbar()
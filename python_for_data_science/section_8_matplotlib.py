import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 11)
y = x**2

# functional
plt.plot(x, y)
plt.savefig("test.png")

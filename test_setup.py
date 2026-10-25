import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 200)
plt.plot(t, np.sin(t))
plt.title("Setup works")
plt.show()
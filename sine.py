import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 901, 10)        
radians = np.radians(x)         
y = np.sin(radians)

plt.plot(x,y)
plt.xticks(np.arange(0,901,10))
plt.grid()
plt.xlabel("Degree (x) :")
plt.ylabel("Sine(x)")
plt.title("Sine graph :")
plt.show()


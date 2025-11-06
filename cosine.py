import numpy as np
import matplotlib.pyplot as plt

angles=np.arange(0,901,10)
radiant=np.radians(angles)
cosine=np.cos(radiant)

plt.plot(angles,cosine,color='red')
plt.xticks(np.arange(0,901,15))
plt.grid()
plt.xlabel("Angles :")
plt.ylabel("cops(x) :")
plt.title("Cos grapgh :")
plt.show()

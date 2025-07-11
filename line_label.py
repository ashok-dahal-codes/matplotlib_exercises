from matplotlib import pyplot as plt
import numpy as np

xpoints = np.array([0,1,2,3])
ypoints = np.array([1,8,3,10])

plt.plot(xpoints, ypoints)
plt.xlabel("average pulse")
plt.ylabel("calorie burn")
plt.title("sportss watch data")
plt.show()
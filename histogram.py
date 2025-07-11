import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170,10,250)
plt.xlabel("height in cm")
plt.ylabel("frequency of people")
plt.title("student's freqeuncy on the basis of height")
plt.hist(x)
plt.show()
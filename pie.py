import matplotlib.pyplot as plt
import numpy as np

y = np.array([20,30,45,10])
mylabels = ["apples","bananas","pineapple","mangoes"]
#start from first i.e 20 or apple and move to counter clockwise and draw remaining chart comparing the y values
plt.pie(y, labels = mylabels)
plt.show()
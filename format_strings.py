from matplotlib import pyplot as plt
import numpy as np

ypoints = np.array([1,12,4,3])
# the fomrat strings syntax contains marker|line|color, here the marker is circle or o and the line is dotted given by the colon and the color is green given by g but if nothing is given as the color the default is  blue but the line parameter is must to see something
plt.plot(ypoints, "o:g" )
plt.show()

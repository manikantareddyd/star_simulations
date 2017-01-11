import numpy as np
snapshot = np.genfromtxt("data/c_0000.csv", delimiter=',', dtype=None, names=True) 

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(snapshot['vx'], snapshot['vy'], snapshot['vz'])

fig.show()
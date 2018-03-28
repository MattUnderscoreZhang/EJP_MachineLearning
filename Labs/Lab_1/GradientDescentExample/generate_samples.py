import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv

x1 = np.array([np.random.uniform(100) for i in range(100)])
x2 = np.array([np.random.uniform(100) for i in range(100)])
y_truth = 2*x1 + 8*np.exp(x2/25)

noise = np.array([np.random.normal(3) for i in range(100)])
y = y_truth + noise

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x1, x2, y)
ax.set_xlabel("x1")
ax.set_ylabel("x2")
ax.set_zlabel("y")
plt.show()

data_file = open("data.csv", 'w')
data_writer = csv.writer(data_file, delimiter=' ')
data_writer.writerow(x1)
data_writer.writerow(x2)
data_writer.writerow(y)

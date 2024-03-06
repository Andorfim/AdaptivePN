from adaptivepn.Voltage.DensityCharges.Probability.Probability import Probability
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


x = np.linspace(1e-8, 1e-6, 50)
y = np.linspace(1e-8, 5e-7, 50)


s_beam = 1e4
diffusion_length = 1e-6
relationship = 1e7
accuracy = 50


data_x = np.array([])
data_y = np.array([])

for x in x:
    data_x = np.concatenate((data_x, np.linspace(x, x, 50)))
    data_y = np.concatenate((data_y, y))

probability_tool = Probability(diffusion_length=diffusion_length, relationship=relationship)

data_probability = [
    probability_tool.proceed(x=x_val, y=y_val, accuracy=accuracy)
    for x_val in data_x
    for y_val in data_y
]
# TODO уменьшить сложность

data_probability = np.array(data_probability)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(data_x, data_y, data_probability, cmap='viridis')


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
fig.colorbar(surf)


plt.show()

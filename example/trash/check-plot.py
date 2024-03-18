'''

Проверочный файл для наложения функции-плотности вероятности на pn-модель

'''

from example.trash.Probability import Probability
import numpy as np




x = np.linspace(-1e-6, 1e-6, 100)
y = np.linspace(0, 5e-7, 100)


s_beam = 1e4
diffusion_length = 1e-6
relationship = 1e7


data_x = np.array([])
data_y = np.array([])

for boundary in x:
    data_x = np.concatenate((data_x, np.linspace(boundary, boundary, 100)))
    data_y = np.concatenate((data_y, y))

probability_tool = Probability(diffusion_length=diffusion_length, relationship=relationship)


data_probability = []

for i in range(len(data_x)):
    data_probability.append(probability_tool.proceed(x = data_x[i], y = data_y[i]))

data_probability = np.array(data_probability)


data_probability_plot = []

for data in data_probability:
    data_probability_plot.append([data])

data_probability = np.array(data_probability_plot)

#TODO сделать разными цветами по отношению к тому, насколько сильно увеличивается data_probability
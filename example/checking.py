import numpy as np

x = np.linspace(1e-8, 1e-6, 100)
y = np.linspace(1e-8, 5e-7, 100)


# data_x = []

# data_x = np.concatenate((data_x, np.linspace(x[0], x[0], 100)))

data_probability = [
    x_val + y_val
    for x_val in x
    for y_val in y
]

data_probability



'''

Модуль расчета Гаусова пучка при z = 0

1D приближение

'''

import numpy as np


class TEField:

    def __init__(self, amplitude, radius, height):
        self.amplitude = amplitude
        self.radius = radius
        self.height = height

    def proceed(self, x) -> np.array:

        field = []

        for x_i in x:

            field.append(self.amplitude*np.exp(-1*(x_i**2 + self.height**2)/(self.radius**2)))

        return np.array(field)







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
        y_space = np.linspace(-1*self.height, self.height, 3)

        for x_i in x:

            buffer = []

            for y_i in y_space:
                buffer.append(self.amplitude*np.exp(-1*(x_i**2 + y_i**2)/(self.radius**2)))

            field.append(np.std(buffer))

            # field.append(self.amplitude * np.exp(-1 * (x_i ** 2 + self.height ** 2) / (self.radius ** 2)))


        return np.array(field)

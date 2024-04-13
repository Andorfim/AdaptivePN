'''

Модуль расчета Гаусова пучка при z = 0

1D приближение

'''

import numpy as np


class TEField:

    def __init__(self, amplitude, radius, geometry_parameters):
        self.amplitude = amplitude
        self.radius = radius
        self.geometry_parameters = geometry_parameters


    def proceed(self, x):

        field = []

        height_slab = self.geometry_parameters[0]
        height_rib = self.geometry_parameters[1]
        width_rib = self.geometry_parameters[2]

        y_space_rib = np.linspace(-0.5*height_rib, 0.5*height_rib, 3)
        y_space_slab = np.linspace(-0.5*height_slab, 0.5*height_slab, 3)


        for x_i in x:

            buffer = []

            if np.abs(x_i) > width_rib:
                for y_i in y_space_rib:
                    buffer.append(self.amplitude * np.exp(-1 * (x_i ** 2 + y_i ** 2) / (self.radius ** 2)))
            else:
                for y_i in y_space_slab:
                    buffer.append(self.amplitude * np.exp(-1 * (x_i ** 2 + y_i ** 2) / (self.radius ** 2)))

            field.append(np.std(buffer))

        return np.array(field)
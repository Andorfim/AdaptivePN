'''

Модуль расчета эффективного показателя преломления


Основа:
Silicon Photonics Design

'''

import numpy as np

class EffectiveIndex:

    def __init__(self, field, delta_refractive, accuracy: int, boundary):

        self.field = field
        self.delta_refractive = delta_refractive
        self.accuracy = accuracy #опционально 10

        self.boundary = boundary


    def proceed(self):

        effective_index = []
        x_plot = []

        field_square = np.array(self.field)**2
        delta_refractive_square = np.array(self.delta_refractive)


        for i in range(int(len(self.field)-self.accuracy)):

            if i < self.boundary:
                effective_index.append(

                    3.48 + np.dot(field_square[i:i+self.accuracy], delta_refractive_square[i:i+self.accuracy])/np.sum(field_square[i:i+self.accuracy])

                )
            else:
                effective_index.append(3.48)

            x_plot.append(i)

        return [x_plot, effective_index]

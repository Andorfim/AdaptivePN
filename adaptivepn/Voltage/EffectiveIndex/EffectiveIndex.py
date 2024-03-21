'''

Модуль расчета эффективного показателя преломления


Основа:
Silicon Photonics Design

'''

import numpy as np

class EffectiveIndex:

    def __init__(self, field, delta_refractive, accuracy: int, step):

        self.field = field
        self.delta_refractive = delta_refractive
        self.accuracy = accuracy #опционально 10

        self.step = step


    def proceed(self):

        effective_index = []
        x_plot = []

        field_square = np.array(self.field)**2
        field_square_discrete = []
        delta_refractive_discrete = []


        # Дискретизация
        for i in range(len(field_square)-1):
            field_square_discrete.append(
                (field_square[i+1] + field_square[i])*0.5
            )
            delta_refractive_discrete.append(
                (self.delta_refractive[i+1] + self.delta_refractive[i])*0.5
            )

        field_square_on_step = np.array(field_square_discrete)*self.step*0.5
        delta_refractive = np.array(delta_refractive_discrete)

        under_integral = field_square_on_step*delta_refractive

        for i in range(int(len(field_square_on_step)-self.accuracy)):

            if sum(field_square_on_step[i:i+self.accuracy]) != 0:

                buffer_up = []
                buffer_down = []

                for i in range(i, i + self.accuracy):

                    buffer_up.append(
                        (under_integral[i + 1] + under_integral[i]) #Для уменьшения сложности self.step перенес в field_square_on_step
                    )

                    buffer_down.append(
                        (field_square_on_step[i+1] + field_square_on_step[i])
                    )



                effective_index.append(
                    3.48 + np.sum(np.array(buffer_up))/np.sum(np.array(buffer_down))
                )

            else:
                effective_index.append(3.48)

            x_plot.append(i*self.step*self.accuracy/2)

        return [x_plot, effective_index]

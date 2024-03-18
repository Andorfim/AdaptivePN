'''

Модуль расчета электрического поля диффузии


Основа:

Davies, R. L., & Gentry, F. E. (1964). Control of electric field at the surface of P-N junctions. IEEE Transactions on Electron Devices, 11(7), 313–323. doi:10.1109/t-ed.1964.15335


'''
import numpy as np
from scipy.constants import elementary_charge, epsilon_0

class Field:

    def __init__(self, density_charges: list, depletion_width: float, acceptor_density: float, donor_density):
        '''

        :param density_charge:

        '''

        self.density_charges = density_charges
        self.depletion_width = depletion_width
        self.acceptor_density = acceptor_density
        self.donor_density = donor_density

    def proceed(self, step: float, indexes: list, lip: float):

        x_p_i = (lip + indexes[0][1] + step/2)/step
        x_n_i = (lip + indexes[1][0] + step/2)/step



        field_list = []




        for i in range(len(self.density_charges)-1):


            if (i >= x_p_i) and (i <= x_n_i):



                field_list.append(elementary_charge*self.acceptor_density*self.depletion_width/epsilon_0)


            elif i < x_p_i:

                field_list.append(
                    step*np.sum((self.density_charges[:i+1]))
                )


            elif i > x_n_i:
                field_list.append(
                    # step * np.sum((self.density_charges[:int(x_p_i)])) + step*np.sum((self.density_charges[int(x_n_i)+1:i+1]))

                    0
                )

        # Проверить правило Симпсона

        return field_list







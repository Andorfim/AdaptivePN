'''

Модуль расчета электрического поля диффузии


Основа:

Davies, R. L., & Gentry, F. E. (1964). Control of electric field at the surface of P-N junctions. IEEE Transactions on Electron Devices, 11(7), 313–323. doi:10.1109/t-ed.1964.15335
Kazanori Shioda; Toshiharu Oobu; Kenji Kijima (2002). Numerical simulation of thermal runaway phenomena in silicon semiconductor devices. , 31(6), 438–455. doi:10.1002/htj.10044

'''
import numpy as np
from scipy.constants import elementary_charge, epsilon_0, Boltzmann

class Field:

    def __init__(self, density_charges: list, acceptor_density: float, donor_density):
        '''

        :param density_charge:

        '''

        self.density_charges = density_charges
        self.acceptor_density = acceptor_density
        self.donor_density = donor_density

    def proceed(self, indexes, lip: float):


        field_list = []

        x_p_i = (-0.5*indexes[0][1]/lip)*len(self.acceptor_density)
        x_n_i = (0.5*indexes[1][0]/lip)*len(self.acceptor_density)

        for i in range(len(self.acceptor_density)):

            if (i >= x_p_i) and (i <= x_n_i) and self.density_charges[i] != 0:

                field_list.append(
                    (elementary_charge/(epsilon_0))*self.density_charges[i]
                )

            else:

                field_list.append(
                    1
                )

        # Проверить правило Симпсона

        return np.array(field_list)







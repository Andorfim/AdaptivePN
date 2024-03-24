"""

Модуль расчета примеси в PN-соединении для валидации и одномерного представления концентрации


Основано на Silicon Photonics Design
Davies, R. L., & Gentry, F. E. (1964). Control of electric field at the surface of P-N junctions. IEEE Transactions on Electron Devices, 11(7), 313–323. doi:10.1109/t-ed.1964.15335
#Kazanori Shioda; Toshiharu Oobu; Kenji Kijima (2002). Numerical simulation of thermal runaway phenomena in silicon semiconductor devices. , 31(6), 438–455.         doi:10.1002/htj.10044 


"""
import numpy as np
from scipy.constants import Boltzmann, elementary_charge


class DensityCharges:

    def __init__(self, indexes: list, intrinsic_density: float, temperature: float, acceptor_density, donor_density, applied_voltage):

        '''

        :param indexes: list - список индексов-узлов, где есть граница зоны истощения и другая граница (Xp++, Xp, Xn, Xn++) #TODO какая?
        :param density_impurity: [list, list] - список концентраций акцепторов и доноров (строго в таком порядке)
        :param intrinsic_concentration: float - внутренняя концентрация

        '''

        self.indexes = indexes
        self.intrinsic_density = intrinsic_density
        self.acceptor_density = acceptor_density
        self.donor_density = donor_density
        self.temperature = temperature
        self.applied_voltage = applied_voltage

    def proceed(self, x):

        '''

        :param x: положение в пространстве
        :potencial: вольтаж в данной точке
        :return: density charge: Nd - Na + p - n


        '''
        density_charge = []

        # Замена экспоненты
        k = np.exp((self.applied_voltage*elementary_charge/(Boltzmann*self.temperature)) - 1)
        # Замена квадрата intrinisic
        square = (self.intrinsic_density**2)

        electrons_list = []
        holes_list = []


        # Замена для формул; длина волны: 1550 нанометров
        # a = -8.8e-22
        # b = -8.5e-18



        for x_i in x:

            if x_i >= self.indexes[0][0] and x_i < self.indexes[0][1]:

                electrons = ((square / self.acceptor_density)*
                     (1 + k*(1 - (self.indexes[0][1] - x_i)/(self.indexes[0][1] - self.indexes[0][0]))))

                holes = self.acceptor_density

                electrons_list.append(electrons)
                holes_list.append(holes)

                density_charge.append(

                    0

                )

                # density_charge.append(a * electrons + b * (holes**0.8))

            elif x_i > self.indexes[1][0] and x_i <= self.indexes[1][1]:

                electrons = self.donor_density
                holes = (square/self.donor_density) * (1 + k*(1 - (x_i - self.indexes[1][0]) /(self.indexes[0][0] - self.indexes[0][1])))

                # density_charge.append(a * electrons + b * (holes**0.8))

                density_charge.append(

                    0
                )

                electrons_list.append(electrons)
                holes_list.append(holes)

            elif x_i >= self.indexes[0][1] and x_i <= 0:

                density_charge.append(
                    -1*self.acceptor_density*(x_i + self.indexes[0][1])
                )

                electrons_list.append(0)
                holes_list.append(0)


            elif x_i > 0 and x_i <= self.indexes[1][0]:

                density_charge.append(
                    -1*self.donor_density*(x_i - self.indexes[1][0])
                )

                electrons_list.append(0)
                holes_list.append(0)

        return [density_charge, electrons_list, holes_list]



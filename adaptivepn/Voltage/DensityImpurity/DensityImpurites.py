"""

Модуль расчета примеси в PN-соединении для валидации и одномерного представления концентрации


Основано на Silicon Photonics Design
#TODO (тоже ссылаются, потом исправлю)


"""
import numpy as np
from scipy.constants import Boltzmann

class DensityImpurites:

    def __init__(self, indexes: list, density_impurity: list, intrinsic_concentration: float, charge: float, temperature: float):
        '''

        :param indexes: list - список индексов-узлов, где есть граница зоны истощения и другая граница (Xp++, Xp, Xn, Xn++) #TODO какая?
        :param density_impurity: [list, list] - список концентраций акцепторов и доноров (строго в таком порядке)
        :param intrinsic_concentration: float - внутренняя концентрация

        '''

        self.indexes = indexes
        self.intrinsic_concentration = intrinsic_concentration
        self.density_impurity = density_impurity
        self.charge = charge
        self.temperature = temperature

    def proceed(self, x, potencial):

        '''

        :param x: положение в пространстве
        :potencial: вольтаж в данной точке
        :return: list список из концентрации акцепторов и доноров (строго в таком поярдке)

        '''

        if x >= self.indexes[0][0] and x <= self.indexes[0][1]:

            n = ((self.intrinsic_concentration**2 / self.density_impurity[0])*
                 (1 + (1 - (self.indexes[0][1] - x)/(self.indexes[0][1] - self.indexes[0][0]))))*np.exp((potencial*self.charge)/(Boltzmann*self.temperature) - 1) #TODO заменить везде self.charge/(Boltzman*Temperature)

            return [self.density_impurity[0], n]

        elif x > self.indexes[0][1] and x < self.indexes[1][0]:

            return [0, 0]

        elif x >= self.indexes[1][0] and x <= self.indexes[1][1]:

            p = ((self.intrinsic_concentration ** 2 / self.density_impurity[1]) *
                 (1 + (1 - (x - self.indexes[1][0]) / (self.indexes[0][0] - self.indexes[0][1])))) * np.exp(
                (potencial * self.charge) / (
                            Boltzmann * self.temperature) - 1)  # TODO заменить везде self.charge/(Boltzman*Temperature)

            return [p, self.density_impurity[1]]

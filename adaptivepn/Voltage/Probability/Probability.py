'''

Модуль расчета вероятности туннелирования

Основа:
Oldham, W.G.; Samuelson, R.R.; Antognetti, P. (1972). Triggering phenomena in avalanche diodes. , 19(9), 1056–1060. doi:10.1109/t-ed.1972.17544

'''


import numpy as np

class Probability:

    def __init__(self, electric_field: list):

        self.electric_field = electric_field

    def proceed(self):

        # коэффициенты ионизации

        alpha_electron = [3.8e6 * np.exp(-1.75e6 / field) for field in self.electric_field]
        alpha_holes = [2.25e7 * np.exp(-3.26e6 / field) for field in self.electric_field]

        probability_electron = [0]
        probability_holes = []



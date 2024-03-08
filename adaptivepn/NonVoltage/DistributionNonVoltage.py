'''
    Модуль инициализаии распредления носителей при нулевом напряжении между концами PN-соединения

    Выражается в логарифмической шкале

'''

import numpy as np






class DistributionNonVoltage:

    def __init__(self, first_density: float):
        '''
        :param type_distribution: first_density
        '''

        self.first_density = first_density


    def proceed(self, list_indexes: list) -> np.ndarray: #при списке и кортеже одна и та же сложность - 4

        return np.dot(self.first_density, np.ones((list_indexes[0][0], list_indexes[0][1]), int) + np.zeros(
                (list_indexes[1][0], list_indexes[1][1]), int))

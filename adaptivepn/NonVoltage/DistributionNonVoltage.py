'''
    Модуль инициализаии распредления носителей при нулевом напряжении между концами PN-соединения

    Выражатся в логарифмической шкале

'''

import numpy as np



class DistributionNonVoltage:

    def __init__(self, type_distribution: bool, first_density: float):
        '''

        :param type_distribution: тип доппированной части полупроводника: True - P тип, False - N тип
        :param type_distribution: first_density

        '''

        self.type_distribution = type_distribution
        self.first_density = first_density

    def proceed(self, list_indexes: list) -> np.ndarray:

        def hole_distribution(list_indexes) -> np.ndarray: #при списке и кортеже одна и та же сложность - 4
            return np.dot(self.first_density, np.ones((list_indexes[0][0], list_indexes[0][1]), int) + np.zeros(
                (list_indexes[1][0], list_indexes[1][1]), int))

        def electron_distribution(list_indexes) -> np.ndarray:
            return np.dot(self.first_density, np.ones((list_indexes[0][0], list_indexes[0][1]), int) + np.zeros(
                (list_indexes[1][0], list_indexes[1][1]), int))

        if self.type_distribution:
            return hole_distribution(list_indexes)
        else:
            return electron_distribution(list_indexes)

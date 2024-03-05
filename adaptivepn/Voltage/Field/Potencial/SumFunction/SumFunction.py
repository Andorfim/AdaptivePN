'''

Модуль расчета заменяющей функции, которая представляет собой, как сумму
функций примесей и p(x, y), n(x, y) (при side: outside)

Основано на:
Davies, R.L.; Gentry, F.E. (1964). Control of electric field at the surface of P-N junctions. , 11(7), 313–323. doi:10.1109/t-ed.1964.15335 

'''

import numpy as np



class SumFunction:

    def __init__(self):

    def density_acceptors_impurites(self, indexes: list) -> float:
        '''

        :param indexes: list (Список координат)

        '''


        return

    def density_donors_impurites(self, indexes: list) -> float:
        '''

        :param indexes: list (Список координат)

        '''

        return

    def density_holes(self, indexes: list) -> float:
        '''

        :param indexes: list (Список координат)

        '''

        return

    def density_electrons(self, indexes: list) -> float:
        '''

        :param indexes: list (Список координат)

        '''

        return


    def proceed(self, side: str, indexes: list) -> float:
        '''

        :param side: outside (вне зоны истощения), inside (внутри зоны истощения)
        :return: Заменяющая функция
        '''

        if side == 'outside':
            return density_acceptors_impurites(self, indexes) + density_donors_impurites(self, indexes)
        else:
            return (density_acceptors_impurites(self, indexes) + density_donors_impurites(self, indexes)
                    + density_holes(self, indexes) + density_electrons(self, indexes))





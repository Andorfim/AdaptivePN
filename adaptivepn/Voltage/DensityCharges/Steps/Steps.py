'''

Модуль расчета новых шагов

Подсчет новых шагов обеспечивает уменьшению общего количества узлов в сетке


Математику написал сам

Основная идея: на основе гладкости градиента делать решение уменьшать/оставлять/увеличивать количество узлов

'''
from adaptivepn.Voltage.DensityCharges.Probability.Probability import Probability
import numpy as np

# Попробовать уменьшать узлы до определенной ошибки


class Steps:

    def __init__(self, probability, data_x, data_y):

        self.probability = probability
        self.data_x = data_x
        self.data_y = data_y


    def proceed(self, quantity: int, epsilon: float):

        def gradient(index):


            probability_all = []


            for sublist in self.probability:
                probability_all.extend(sublist)



            period = int(np.sqrt(len(self.probability)))



            probability_up_i = probability_all[index + period]
            probability_down_i = probability_all[index - period]

            probability_up_j = probability_all[index + 1]
            probability_down_j = probability_all[index - 1]

            return 0.5*( probability_up_i - probability_down_i + probability_up_j - probability_down_j)



        def procedure_deleting(index):

            self.data_x[index] = 0
            self.data_y[index] = 0


        list_indexes_delete = []



        for _ in range(quantity):

            index = np.random.randint(0, len(self.probability))

            if gradient(index=index) > epsilon:

                while gradient(index) < epsilon:

                    index = np.random.randint(0, len(self.probability))

                list_indexes_delete.append(index)

            else:
                list_indexes_delete.append(index)


            for index in list_indexes_delete:
                procedure_deleting(index)

        return [self.probability, self.data_x, self.data_y]

# TODO подумать, как сделать, чтобы не занулять data_x(_y)
# TODO подумать что делать при большом параметре quantity (также странно себя ведет функция probability c нулевыми значениями)




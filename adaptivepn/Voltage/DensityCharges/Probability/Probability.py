'''

Модуль расчета вероятности обнаружения носителей

Основано на:

Moore, J. E., Affouda, C. A., Maximenko, S. I., & Jenkins, P. (2018). Analytical and numerical simulation of electron beam induced current profiles in p-n junctions. Journal of Applied Physics, 124(11), 113102. doi:10.1063/1.5049117
Bonard, Jean‐Marc; Ganière, Jean‐Daniel (1996). Quantitative analysis of electron‐beam‐induced current profiles across p–n junctions in GaAs/Al0.4Ga0.6As heterostructures. Journal of Applied Physics, 79(9), 6987–6994. doi:10.1063/1.361464
Donolato, C. (1994). Reciprocity theorem for charge collection by a surface with finite collection velocity: Application to grain boundaries. Journal of Applied Physics, 76(2), 959–966. doi:10.1063/1.357774


'''

#TODO Фурье преобразование, ориентироваться на Moore

import numpy as np
from scipy.fftpack import fft, fftfreq


class Probability:

    def __init__(self, diffusion_length: float, relationship: float):

        self.relationship = relationship
        self.diffusion_length = diffusion_length


    def proceed(self, x: float, y: float, accuracy: int):


        k = np.linspace(0.1, 2 * np.pi, accuracy, endpoint=False)


        under_integral_function = np.exp(-x*np.sqrt(k**2 + 1/(self.diffusion_length)**2)) * (
                np.cos(k*y) + np.sin(k*y) * (self.relationship/k))/(k**2 + (self.relationship)**2)

        fourier_transform = fft(under_integral_function)

        N = len(fourier_transform)
        dk = k[1] - k[0]

        return fftfreq(N, dk)
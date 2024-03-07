'''

Модуль расчета carrier generation rate

Основано на:

Bonard, Jean‐Marc; Ganière, Jean‐Daniel (1996). Quantitative analysis of electron‐beam‐induced current profiles across p–n junctions in GaAs/Al0.4Ga0.6As heterostructures. Journal of Applied Physics, 79(9), 6987–6994. doi:10.1063/1.361464

'''


import numpy as np

class CarrierGenerationRate:

    def __init__(self, sigma_x: float, sigma_y: float):

        self.sigma_x = sigma_x
        self.sigma_y = sigma_y


    def proceed(self, x: float, y: float) -> float:

        return ((2*np.sqrt(np.pi)*self.sigma_x * (self.sigma_y**3))**(-1) *
                np.exp(-x**2 * self.sigma_x ** (-2))) * np.exp(-1*y*(self.sigma_x**(-1))) * (y**2)

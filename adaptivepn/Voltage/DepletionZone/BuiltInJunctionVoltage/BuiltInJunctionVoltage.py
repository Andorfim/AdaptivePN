'''

Модуль расчета встроенного напряжения перехода

Основано на:

Simple Model for Carrier Densities in the Depletion Region of p-n Junctions



'''


import numpy as np
from scipy.constants import Boltzmann


class BuiltInJunctionVoltage:

    def __init__(self, temperature, charge, density_unperturbed_n_type, density_unperturbed_p_type):
        self.temperature = temperature
        self.charge = charge
        self.density_unperturbed_n_type = density_unperturbed_n_type
        self.density_unperturbed_p_type = density_unperturbed_p_type

    def proceed(self):
        return (Boltzmann*self.temperature/self.charge)*np.log(self.density_unperturbed_n_type/self.density_unperturbed_p_type)


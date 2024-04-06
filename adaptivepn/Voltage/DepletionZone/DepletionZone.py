'''

Модуль расчета ширины истощенной зоны

Основано на:

Simple Model for Carrier Densities in the Depletion Region of p-n Junctions


'''
import numpy as np
from scipy.constants import physical_constants, Boltzmann, elementary_charge, epsilon_0


class DepletionZone:

    def __init__(self, temperature, applied_voltage, acceptor_density, donor_density, intrinsic_density, pn_offset):
        '''

        :param temperature: Температура среды
        :param density_unperturbed_n_type: плотность невозмущенной n части
        :param density_unperturbed_p_type: плотность невозмущенной p части
        :param applied_voltage: приложенное напряжение
        :param ionized_acceptor_density: плотность ионизованных дырок
        :param ionized_donor_density: плотность ионизованных электронов


        '''

        self.applied_voltage = applied_voltage
        self.acceptor_density = acceptor_density
        self.donor_density = donor_density
        self.temperature = temperature
        self.intrinsic_density = intrinsic_density
        self.pn_offset = pn_offset


    @property
    def proceed(self):

        def x_p(depletion_width):
            return self.pn_offset - 1*depletion_width/(1 + self.acceptor_density/self.donor_density)

        def x_n(depletion_width):
            return self.pn_offset + depletion_width / (1 + self.donor_density / self.acceptor_density)


        built_in_junction_voltage = (Boltzmann*self.temperature/elementary_charge)*np.log((self.donor_density*self.acceptor_density)/(self.intrinsic_density**2))




        #relative permittivity = 11.8 для кремния


        depletion_width = np.sqrt((2 * 11.8 * (built_in_junction_voltage - self.applied_voltage) * epsilon_0 * (self.acceptor_density + self.donor_density))/(elementary_charge*self.acceptor_density*self.donor_density))

        return [x_p(depletion_width), x_n(depletion_width)]




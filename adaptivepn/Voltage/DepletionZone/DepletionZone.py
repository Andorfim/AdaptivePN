'''

Модуль расчета ширины истощенной зоны

Основано на:

Simple Model for Carrier Densities in the Depletion Region of p-n Junctions


'''
import numpy as np
from adaptivepn.Voltage.DepletionZone.BuiltInJunctionVoltage.BuiltInJunctionVoltage import BuiltInJunctionVoltage
from scipy.constants import physical_constants

class DepletionZone:

    def __init__(self, temperature, density_unperturbed_n_type, density_unperturbed_p_type, applied_voltage, ionized_acceptor_density, ionized_donor_density, charge):
        '''

        :param temperature: Температура среды
        :param density_unperturbed_n_type: плотность невозмущенной n части
        :param density_unperturbed_p_type: плотность невозмущенной p части
        :param applied_voltage: приложенное напряжение
        :param ionized_acceptor_density: плотность ионизованных дырок
        :param ionized_donor_density: плотность ионизованных электронов
        :param charge: заряд

        '''

        self.applied_voltage = applied_voltage
        self.ionized_acceptor_density = ionized_acceptor_density
        self.ionized_donor_density = ionized_donor_density
        self.temperature = temperature
        self.density_unperturbed_n_type = density_unperturbed_n_type
        self.density_unperturbed_p_type = density_unperturbed_p_type
        self.charge = charge


    def proceed(self, side: bool, normalization_factor: float) -> int:

        def x_p(self, built_in_junction_voltage):
            return np.sqrt((2 * physical_constants["electric constant"] / self.charge) * (
                        built_in_junction_voltage - self.applied_voltage) * self.ionized_acceptor_density / (
                                       self.ionized_donor_density * (
                                           self.ionized_donor_density + self.ionized_acceptor_density)))

        def x_n(self, built_in_junction_voltage):
            return np.sqrt((2 * physical_constants["electric constant"] / self.charge) * (
                        built_in_junction_voltage - self.applied_voltage) * self.ionized_donor_density / (
                                       self.ionized_acceptor_density * (
                                           self.ionized_donor_density + self.ionized_acceptor_density)))

        built_in_junction_voltage = BuiltInJunctionVoltage(temperature=self.temperature,
                                                           charge=self.charge,
                                                           density_unperturbed_n_type=self.density_unperturbed_n_type,
                                                           density_unperturbed_p_type=self.density_unperturbed_p_type)

        if side:
            return int(x_p(self, built_in_junction_voltage=built_in_junction_voltage)/normalization_factor)

        else:
            return int(x_n(self, built_in_junction_voltage=built_in_junction_voltage)/normalization_factor)

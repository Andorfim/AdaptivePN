'''

Модуль расчета сдвига фазы


Возвращает зависимость сдвига фазы (Град/мм) от приложенного обратного напряжения (Вольт)


'''

from adaptivepn.Voltage.DensityCharges.DensityCharges import DensityCharges
from adaptivepn.Voltage.DepletionZone.DepletionZone import DepletionZone
from adaptivepn.Voltage.DeltaRefractive.DeltaRefractive import DeltaRefractive
from adaptivepn.Voltage.TEField.TEField import TEField

import numpy as np


class PhaseShift:

    def __init__(self, applied_voltage, temperature,
                 intrinsic_density, acceptor_density,
                 donor_density, pn_offset, x, N, wavelength,
                 amplitude, radius, index_before, geometry_parameters
                 ):

        # for computing
        self.applied_voltage = applied_voltage
        self.temperature = temperature
        self.intrinsic_density = intrinsic_density
        self.acceptor_density = acceptor_density
        self.donor_density = donor_density
        self.pn_offset = pn_offset
        self.x = x
        self.N = N
        self.wavelength = wavelength

        # for TE
        self.amplitude = amplitude
        self.radius = radius

        # for material
        self.index_before = index_before

        # for geometry
        self.geometry_parameters = geometry_parameters


    def proceed(self):

        effective_index_by_voltage = []
        applied_voltage_clear = []




        for applied_voltage_i in self.applied_voltage:

            try:
                depletion_tool = DepletionZone(
                    applied_voltage=applied_voltage_i, acceptor_density=self.acceptor_density,
                    donor_density=self.donor_density,
                    temperature=self.temperature, intrinsic_density=self.intrinsic_density, pn_offset=self.pn_offset
                )

                x_p, x_n = depletion_tool.proceed

                density_charges_tool = DensityCharges(
                    indexes=[[np.min(self.x), x_p], [x_n, np.max(self.x)]],
                    intrinsic_density=self.intrinsic_density,
                    acceptor_density=self.acceptor_density,
                    donor_density=self.donor_density,
                    temperature=self.temperature,
                    applied_voltage=applied_voltage_i
                )

                x = np.linspace(np.min(self.x), np.max(self.x), self.N - 1)

                density_charges_result = density_charges_tool.proceed(x=x)

                delta_refractive_tool = DeltaRefractive(
                    electrons=density_charges_result[1],
                    holes=density_charges_result[2],
                    wavelength=self.wavelength
                )

                delta_refractive_result = delta_refractive_tool.proceed()

                refractive_before = np.linspace(self.index_before, self.index_before, len(delta_refractive_result[0]))

                delta_refractive_result = delta_refractive_result[0] + delta_refractive_result[1] - refractive_before

                te_field_tool = TEField(
                    amplitude=self.amplitude,
                    radius=self.radius,
                    geometry_parameters=self.geometry_parameters
                )

                iter_xp = int((np.max(x) - 2*self.radius) * self.N / (2 * np.max(x)))
                iter_xn = int((np.max(x) + 2*self.radius) * self.N / (2 * np.max(x)))

                quantity_dots_for_te = iter_xn - iter_xp + 1

                x = np.linspace(-2 * self.radius, 2*self.radius, quantity_dots_for_te)

                te_field_result = te_field_tool.proceed(x=x)

                effective_index_by_voltage.append(

                    np.dot(
                        te_field_result ** 2, delta_refractive_result[iter_xp:iter_xn + 1]
                    ) / np.sum(te_field_result ** 2)

                )



                applied_voltage_clear.append(applied_voltage_i)

            except ValueError:
                break



        return [applied_voltage_clear,
                (effective_index_by_voltage - effective_index_by_voltage[
                    len(effective_index_by_voltage) - 1]) * 0.2 * 57.3 / (self.wavelength * 10)]

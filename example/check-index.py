from adaptivepn.Voltage.DensityCharges.DensityCharges import DensityCharges
from adaptivepn.Voltage.DepletionZone.DepletionZone import DepletionZone
from adaptivepn.Voltage.Field.Field import Field
from adaptivepn.Voltage.EffectiveIndex.EffectiveIndex import EffectiveIndex
from adaptivepn.Voltage.DeltaRefractive.DeltaRefractive import DeltaRefractive
from adaptivepn.Voltage.TEField.TEField import TEField

import numpy as np
import matplotlib.pyplot as plt


# Инициализирую необходимые параметры
N = 50000 # Количество точек
#TODO проблема с подгоном, так как шаг выше чем координата границы зоны истощения

x = np.linspace(-1e-6, 1e-6, N)
step = (np.max(x)-np.min(x))/(N-1)

temperature = 25+273.15 # В Кельвинах
intrinsic_density = 8.3e15
acceptor_density = 5e23
donor_density = 5e23
applied_voltage = np.linspace(-5, 0, 500)
pn_offset = 0


effective_index_by_voltage = []
applied_voltage_clear = []


for applied_voltage_i in applied_voltage:

    try:
        depletion_tool = DepletionZone(
            applied_voltage = applied_voltage_i, acceptor_density = acceptor_density, donor_density = donor_density,
            temperature = temperature, intrinsic_density = intrinsic_density, pn_offset = pn_offset
        )

        x_p, x_n = depletion_tool.proceed

        density_charges_tool = DensityCharges(
            indexes=[[-1e-6, x_p], [x_n, 1e-6]],
            intrinsic_density = intrinsic_density,
            acceptor_density=acceptor_density,
            donor_density=donor_density,
            temperature = temperature,
            applied_voltage=applied_voltage_i
        )

        x = np.linspace(-1e-6, 1e-6, N-1)

        density_charges_result = density_charges_tool.proceed(x=x)

        delta_refractive_tool = DeltaRefractive(
            electrons=density_charges_result[1],
            holes=density_charges_result[2],
            wavelength= 1550e-9
        )

        delta_refractive_result = delta_refractive_tool.proceed()

        refractive_before = np.linspace(3.48, 3.48, len(delta_refractive_result[0]))

        delta_refractive_result = delta_refractive_result[0] + delta_refractive_result[1] - refractive_before


        te_field_tool = TEField(
            amplitude = 6e7,
            radius = 250e-9,
            height = 125e-9
        )

        iter_xp = int((1e-6 - 2.5e-7)*N/2e-6)
        iter_xn = int((1e-6 + 2.5e-7)*N/2e-6)

        quantity_dots_for_te = iter_xn - iter_xp + 1

        x = np.linspace(-2.5e-7, 2.5e-7, quantity_dots_for_te)

        te_field_result = te_field_tool.proceed(x=x)

        effective_index_by_voltage.append(

            np.dot(
                te_field_result**2, delta_refractive_result[iter_xp:iter_xn+1]
            )/np.sum(te_field_result**2)

        )

        applied_voltage_clear.append(applied_voltage_i)

    except ValueError:
        break



# phase = (effective_index_by_voltage - effective_index_by_voltage[len(effective_index_by_voltage)-1])*0.02*57.3/1550e-6

plt.title('Change phase shift by voltage')
plt.xlabel('Voltage')
plt.ylabel('Phase shift grad/mm')
plt.xlim(-5, 0)
plt.ylim(0, 65)
plt.plot(applied_voltage_clear, (effective_index_by_voltage - effective_index_by_voltage[len(effective_index_by_voltage)-1])*0.2*57.3/(1550e-8))

plt.show()
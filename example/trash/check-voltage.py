from adaptivepn.Voltage.DensityCharges.DensityCharges import DensityCharges
from adaptivepn.Voltage.DepletionZone.DepletionZone import DepletionZone
from adaptivepn.Voltage.Field.Field import Field
from adaptivepn.Voltage.EffectiveIndex.EffectiveIndex import EffectiveIndex
from adaptivepn.Voltage.DeltaRefractive.DeltaRefractive import DeltaRefractive


import numpy as np
import matplotlib.pyplot as plt


# Инициализирую необходимые параметры
N = 50000 # Количество точек
#TODO проблема с подгоном, так как шаг выше чем координата границы зоны истощения

x = np.linspace(-1*2e-6, 2e-6, N)
step = (np.max(x)-np.min(x))/(N-1)

temperature = 25+273.15 # В кельвинах
# intrinsic_density = 5.29e25 * ((temperature/300)**2.54)*np.exp(-6726/temperature) # 9.7e15
intrinsic_density = 10
acceptor_density = 3e21
donor_density = 2e18
applied_voltage = np.linspace(1.9, 2, 100)

def get_data(applied_voltage):

    depletion_tool = DepletionZone(
        applied_voltage = applied_voltage, acceptor_density = acceptor_density, donor_density = donor_density,
        temperature = temperature, intrinsic_density = intrinsic_density
    )

    x_p, x_n = depletion_tool.proceed

    density_charges_tool = DensityCharges(
        indexes=[[-2e-6, x_p], [x_n, 2e-6]],
        intrinsic_density = intrinsic_density,
        acceptor_density=acceptor_density,
        donor_density=donor_density,
        temperature = temperature,
        applied_voltage=applied_voltage
    )


    density_charges_result = density_charges_tool.proceed([-1.5e-6])



    delta_refractive_tool = DeltaRefractive(
        electrons = density_charges_result[1],
        holes = density_charges_result[2],
        wavelength = 1550e-9
    )

    return delta_refractive_tool.proceed()



data_refractive = []

for voltage in applied_voltage:

    data = get_data(
        applied_voltage=voltage
        )

    data_refractive.append(data[0] + data[1])

plt.title('Change applied voltage')
plt.xlabel('Voltage')
plt.ylabel('delta n')
plt.plot(applied_voltage, data_refractive, 'ro')
plt.show()
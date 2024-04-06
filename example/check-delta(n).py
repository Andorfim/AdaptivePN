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

x = np.linspace(-1e-6, 1e-6, N)
step = (np.max(x)-np.min(x))/(N-1)

temperature = 25+273.15 # В Кельвинах

intrinsic_density = 1e16
acceptor_density = np.linspace(1e23, 1e26, 10000)
donor_density = np.linspace(1e23, 1e26, 10000)
applied_voltage = -1
pn_offset = 0

def get_data(acceptor_density_i, donor_density_i):

    depletion_tool = DepletionZone(
        applied_voltage = applied_voltage, acceptor_density = acceptor_density_i, donor_density = donor_density_i,
        temperature = temperature, intrinsic_density = intrinsic_density, pn_offset = pn_offset
    )

    x_p, x_n = depletion_tool.proceed
    print(x_p, x_n)
    density_charges_tool = DensityCharges(
        indexes=[[-1e-6, x_p], [x_n, 1e-6]],
        intrinsic_density = intrinsic_density,
        acceptor_density=acceptor_density_i,
        donor_density=donor_density_i,
        temperature = temperature,
        applied_voltage=applied_voltage
    )

    density_charges_result = density_charges_tool.proceed([-1e-6])

    delta_refractive_tool = DeltaRefractive(
        electrons=density_charges_result[1],
        holes=density_charges_result[2],
        wavelength=1550e-9
    )

    return delta_refractive_tool.proceed()



data_refractive_acceptor = []
data_refractive_donor = []

for i in range(len(donor_density)):

    data = get_data(
        acceptor_density_i=acceptor_density[i],
        donor_density_i = donor_density[i]
        )

    data_refractive_acceptor.append(data[0]) # electrons
    data_refractive_donor.append(data[1]) # holes


data_refractive_acceptor = data_refractive_acceptor
data_refractive_donor = data_refractive_donor


plt.title('Change carrier concentration')
plt.xlabel('Carrier Density, m^-3 (blue - acceptor, red - donor)')
plt.ylabel('-delta n (by electrons; holes)')

plt.loglog(donor_density, np.dot(data_refractive_donor, -1), 'ro')
plt.loglog(acceptor_density, np.dot(data_refractive_acceptor, -1), 'bo')

plt.show()
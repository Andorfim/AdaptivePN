from adaptivepn.Voltage.DensityCharges.DensityCharges import DensityCharges
from adaptivepn.Voltage.DepletionZone.DepletionZone import DepletionZone
from adaptivepn.Voltage.Field.Field import Field


import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import hbar, Boltzmann

# Инициализирую необходимые параметры
N = 100000 # Количество точек
# #TODO проблема с подгоном, так как шаг выше чем координата границы зоны истощения

x = np.linspace(-1*2e-6, 2e-6, N)
step = (np.max(x)-np.min(x))/(N-1)



y = []

for i in range(N-1):

    if i >= (2e-6-0.5e-6)/step and i <= (2e-6 + 0.5e-6)/step:
        y.append(300e-6)
    else:
        y.append(150e-6)







temperature = 300 #В кельвинах
intrinsic_density = 5.29e25 * ((temperature/300)**2.54)*np.exp(-6726/temperature) # 9.7e15
acceptor_density = 1e21
donor_density = 1e22
applied_voltage = 0.65639


depletion_tool = DepletionZone(
    applied_voltage = applied_voltage, acceptor_density = acceptor_density, donor_density = donor_density,
    temperature = temperature, intrinsic_density = intrinsic_density
)

x_p, x_n = depletion_tool.proceed()

density_charges_tool = DensityCharges(
    indexes=[[-2e-6, x_p], [x_n, 2e-6]],
    intrinsic_density = intrinsic_density,
    acceptor_density=acceptor_density,
    donor_density=donor_density,
    temperature = temperature,
    applied_voltage=applied_voltage
)


density_charges = density_charges_tool.proceed(x)

density_norm = []

max_min = np.max(density_charges) - np.min(density_charges)

min_on_max = np.min(density_charges)/max_min

for density in density_charges:
    density_norm.append(

        density/max_min - min_on_max

    )





field_tool = Field(
    density_charges = density_charges,
    depletion_width = x_n-x_p,
    acceptor_density = acceptor_density,
    donor_density = density_norm #заменил на нормировочные парамтры
)



field = np.array(field_tool.proceed(step=step, indexes=[[-2e-6, x_p], [x_n, 2e-6]], lip=2e-6))
#
#
#
#
#
#
#
#
#
# # Дискретизация области x
x_i = []

for i in range(N-1):

    x_i.append(
        (x[i+1]+x[i])/2
    )

#TODO сделать замену в расчетах (нормировать значения)

# Построение гистограммы
field = field/np.max(field)


colors = plt.cm.viridis(field)

plt.title('Распределение электрического поля диффузии в pn-соединении (Нормированное, 1D приближение для концентраций носителей)')

plt.bar(x_i, y, width=step, color = colors)


plt.ylim(0, np.max(y)*1.1)
plt.show()

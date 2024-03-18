from adaptivepn.Voltage.DensityCharges.DensityCharges import DensityCharges
from adaptivepn.Voltage.DepletionZone.DepletionZone import DepletionZone
from adaptivepn.Voltage.Field.Field import Field
from adaptivepn.Voltage.EffectiveIndex.EffectiveIndex import EffectiveIndex
from adaptivepn.Voltage.DeltaRefractive.DeltaRefractive import DeltaRefractive


import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import hbar, Boltzmann

# Инициализирую необходимые параметры
N = 100000 # Количество точек
# #TODO проблема с подгоном, так как шаг выше чем координата границы зоны истощения

x = np.linspace(-1*2e-6, 2e-6, N)
step = (np.max(x)-np.min(x))/(N-1)



# y = []

# for i in range(N-1):
#
#     if i >= (2e-6-0.5e-6)/step and i <= (2e-6 + 0.5e-6)/step:
#         y.append(300e-6)
#     else:
#         y.append(150e-6)







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

print('depletion_tool has gave result')

density_charges_tool = DensityCharges(
    indexes=[[-2e-6, x_p], [x_n, 2e-6]],
    intrinsic_density = intrinsic_density,
    acceptor_density=acceptor_density,
    donor_density=donor_density,
    temperature = temperature,
    applied_voltage=applied_voltage
)



density_charges_result = density_charges_tool.proceed(x)
print('density_charges_tool has gave result')

density_charges = density_charges_result[0]



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



print('field has  gave result')




# Нормирование электрического поля диффузии
field = field/np.max(field)



delta_refractive_tool = DeltaRefractive(
    electrons = density_charges_result[1],
    holes = density_charges_result[2],
    wavelength = 1550e-9
)


delta_refractive = delta_refractive_tool.proceed()


print('delta refractive tool has gave result')

effective_index_tool = EffectiveIndex(
    field = field,
    delta_refractive = delta_refractive,
    accuracy = 10,  # опционально 10
    boundary = int((2e-6 - x_n)/step)
)

effective_index_result = effective_index_tool.proceed()

print('effective index tool has  gave result')

y = []

effective_index_result_discrete = []
x_i = []

for i in range(len(effective_index_result[1])-1):
    effective_index_result_discrete.append(effective_index_result[1][i+1] + effective_index_result[1][i])
    x_i.append(effective_index_result[0][i+1] + effective_index_result[0][i])


effective_index_result_discrete = 0.5*np.array(effective_index_result_discrete)
effective_index_result_discrete = effective_index_result_discrete/np.max(effective_index_result_discrete)

x_i_discrete = 0.5*step*np.array(x_i)



N = len(x_i_discrete)

for i in range(N):

    if i >= int((1.5e-6)/step) and i <= int((2.5e-6)/(step)): #10 - accuracy
        y.append(300e-6)
    else:
        y.append(150e-6)




colors = plt.cm.viridis(effective_index_result_discrete)
plt.title('Распределение эффективного показателя преломления')
plt.bar(x_i_discrete, y, width=10*step, color = colors)
plt.ylim(0, np.max(y)*1.1)

plt.show()

from adaptivepn.Voltage.DensityCharges.DensityCharges import DensityCharges
from adaptivepn.Voltage.DepletionZone.DepletionZone import DepletionZone
from adaptivepn.Voltage.Field.Field import Field
from adaptivepn.Voltage.EffectiveIndex.EffectiveIndex import EffectiveIndex
from adaptivepn.Voltage.DeltaRefractive.DeltaRefractive import DeltaRefractive


import numpy as np
import matplotlib.pyplot as plt

# Инициализирую необходимые параметры
N = 10000 # Количество точек
# #TODO проблема с подгоном, так как шаг выше чем координата границы зоны истощения

x = np.linspace(-1*2e-6, 2e-6, N)
step = (np.max(x)-np.min(x))/(N-1)



temperature = 270 #В кельвинах
intrinsic_density = 5.29e25 * ((temperature/300)**2.54)*np.exp(-6726/temperature) # 9.7e15
acceptor_density = 6e15
donor_density = 2.5e7
applied_voltage = 1e-4


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


field_tool = Field(
    density_charges = density_charges,
    depletion_width = x_n-x_p,
    acceptor_density = acceptor_density,
    donor_density = donor_density
)



field = np.array(field_tool.proceed(step=step, indexes=[[-2e-6, x_p], [x_n, 2e-6]], lip=2e-6))



print('field has  gave result')


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
    accuracy =  100,  # опционально 10
    step = step
)

effective_index_result = np.array(effective_index_tool.proceed())

print('effective index tool has  gave result')

y = []
x = []

N = len(effective_index_result[0])



for i in range(N):

    if i >= int((1.5e-6)/step) and i <= int((2.5e-6)/(step)): #10 - accuracy
        y.append(300e-6)
    else:
        y.append(150e-6)




colors = plt.cm.viridis(effective_index_result[1]/np.max(effective_index_result[1]))

plt.title('Распределение эффективного показателя преломления')
bars = plt.bar(effective_index_result[0], y, width=100*step, color = colors)

plt.xlabel('x')
plt.ylabel('y')

plt.ylim(0, np.max(y)*1.1)

cbar = plt.colorbar(plt.cm.ScalarMappable(cmap=plt.cm.viridis), ax=plt.gca())
cbar.set_label('Нормированное значение показателя преломления')


plt.show()



# Локализованное распределение
# colors = plt.cm.viridis(effective_index_result[1][4900:5002] / np.max(effective_index_result[1][4900:5002]))
# plt.title('Распределение эффективного показателя преломления (область обеднения)')
# bars = plt.bar(effective_index_result[0][4900:5002], y[4900:5002], width=100*step, color=colors)
#
# plt.xlabel('x')
# plt.ylabel('y')
#
# plt.ylim(0, np.max(y)*1.1)
#
# # Добавление шкалы цветов с использованием цветовой карты
# cbar = plt.colorbar(plt.cm.ScalarMappable(cmap=plt.cm.viridis), ax=plt.gca())
# cbar.set_label('Нормированное значение показателя преломления')
#
# plt.show()
#


# 4900
# 5002




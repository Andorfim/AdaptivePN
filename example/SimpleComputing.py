'''

Пример использования инструмента PhaseShift

'''

from adaptivepn.PhaseShift.PhaseShift import PhaseShift
import matplotlib.pyplot as plt
import numpy as np
import time


start_time = time.time()


# Инициализирую необходимые параметры
N = 50000 # Количество точек


# Геометрия устройства
x = np.linspace(-1e-6, 1e-6, N) #Задаем одномерную сетку для крайних точек соединения
step = (np.max(x)-np.min(x))/(N-1)

height_slab = 100e-9
height_rib = 250e-9 #Высота волновода
width_rib = 500e-9

geometry_parameters = [height_slab, height_rib, width_rib]

temperature = 25+273.15 # В Кельвинах
intrinsic_density = 8.3e15 # Концентрация частиц в валентной зоне


# Списки концентраций дырок и доноров
acceptor_density = [1e23, 5e23, 1e24]
donor_density = [1e23, 5e23, 1e24]

# Приложенное напряжение для обратного смещения (Меньше нуля!)
applied_voltage = np.linspace(-5, 0, 500)
pn_offset = 0

# Параметры Гауссова Пучка
wavelength = 1550e-9 #Длина волны
amplitude = 6e7 #Амплитуда
radius = 250e-9 #Радиус Гауссовского пучка по уровню интенсивности 1/exp(2) от амплитуды


index_before = 3.48 #Показатель преломления материала до допирования и подключения напряжения

data = []

for i in range(len(donor_density)):
    phase_shift_tool = PhaseShift(
        applied_voltage = applied_voltage, temperature=temperature,
        intrinsic_density=intrinsic_density, acceptor_density=acceptor_density[i],
        donor_density=donor_density[i], pn_offset=pn_offset, x=x, N=N, wavelength=wavelength,
        amplitude=amplitude, radius=radius, index_before=index_before, geometry_parameters=geometry_parameters
    )

    data.append(phase_shift_tool.proceed())

end_time = time.time()


plt.title('Change phase shift by voltage (green - doping: 1e18 cm^-3, orange - doping: 5e17 cm^-3, blue - doping: 1e17 cm^-3)')
plt.xlabel('Voltage')
plt.ylabel('Phase shift grad/mm')

for info in data:

    plt.plot(info[0], info[1])
    plt.xlim(-5, 0)
    plt.ylim(0, 100)


plt.show()


print(end_time - start_time)


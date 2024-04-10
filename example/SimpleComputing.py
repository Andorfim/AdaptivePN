'''

Пример использования инструмента PhaseShift

'''

from adaptivepn.PhaseShift.PhaseShift import PhaseShift
import matplotlib.pyplot as plt
import numpy as np




# Инициализирую необходимые параметры
N = 50000 # Количество точек

x = np.linspace(-1e-6, 1e-6, N)
step = (np.max(x)-np.min(x))/(N-1)

temperature = 25+273.15 # В Кельвинах
intrinsic_density = 8.3e15


acceptor_density = [1e23, 5e23, 1e24]
donor_density = [1e23, 5e23, 1e24]


applied_voltage = np.linspace(-5, 0, 500)
pn_offset = 0


wavelength = 1550e-9
amplitude = 6e7
radius = 250e-9
height = 125e-9

index_before = 3.48

data = []

for i in range(len(donor_density)):
    phase_shift_tool = PhaseShift(
        applied_voltage = applied_voltage, temperature=temperature,
        intrinsic_density=intrinsic_density, acceptor_density=acceptor_density[i],
        donor_density=donor_density[i], pn_offset=pn_offset, x=x, N=N, wavelength=wavelength,
        amplitude=amplitude, radius=radius, height=height, index_before=index_before
    )

    data.append(phase_shift_tool.proceed())


plt.title('Change phase shift by voltage (green - doping: 1e18 cm^-3, orange - doping: 5e17 cm^-3, blue - doping: 1e17 cm^-3)')
plt.xlabel('Voltage')
plt.ylabel('Phase shift grad/mm')

for info in data:

    plt.plot(info[0], info[1])
    plt.xlim(-5, 0)
    plt.ylim(0, 100)


plt.show()
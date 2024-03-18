'''

Модуль расчета изменения показателя преломления



Основа:
Silicon Photonics Design (См там источник)

'''

import numpy as np

class DeltaRefractive:

    def __init__(self, electrons, holes, wavelength):
        '''

        :param electrons: концентрация электронов
        :param holes: концентрация дырок
        :param wavelength: длина волны приходящего электромагнитного поля
        '''
        self.electrons = electrons
        self.holes = holes
        self.wavelength = wavelength
    def proceed(self):



        return (self.wavelength**2)*((-1*3.64e-10)*np.array(self.electrons) - (3.51e-6)*(np.array(self.holes))**0.8)


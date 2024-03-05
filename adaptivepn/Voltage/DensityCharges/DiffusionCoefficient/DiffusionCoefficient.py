'''

Модуль расчета коэффициента Диффузии

Основано на:

Bonard, Jean‐Marc; Ganière, Jean‐Daniel (1996). Quantitative analysis of electron‐beam‐induced current profiles across p–n junctions in GaAs/Al0.4Ga0.6As heterostructures. Journal of Applied Physics, 79(9), 6987–6994. doi:10.1063/1.361464

'''


class DiffusionCoefficient:

    def __init__(self, diffusion_length, carrier_lifetime):

        self.diffusion_length = diffusion_length
        self.carrier_lifetime = carrier_lifetime

    def proceed(self):
        return self.diffusion_length**2 / self.carrier_lifetime




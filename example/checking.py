import numpy as np



u = np.linspace(-100, 100, 100)
v = np.linspace(-100, 100, 100)

U, V = np.meshgrid(u, v)
X=U*V
Y=U
Z = V*V

x = 0
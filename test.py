from scipy import integrate
from scipy.special import erf
import numpy as np
gaussian= lambda x: 1/np.sqrt(np.pi)* np.exp(-x**2)
result = integrate.romberg(gaussian, 0, 1, show=True)
print("%g %g" % (2*result , erf(1)))
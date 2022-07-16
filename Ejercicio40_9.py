import numpy as np
import sys

#Sin Numpy
A=range(1000)
print("\nResultado sin Numpy\n")
print(sys.getsizeof(5)*len(A))

#Con Numpy
F=np.array(1000)
print("\nResultado con Numpy\n")
print(F.size*F.itemsize)
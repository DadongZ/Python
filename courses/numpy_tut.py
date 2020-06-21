import numpy as np

a = np.array([1,2,3])
print(a)
b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])

def dprop (dat):
    print([dat, dat.ndim, dat.dtype, dat.size, dat.nbytes, dat.itemsize])

print(dprop(a))
print(dprop(b))

a = np.random.rand(3,3)
print(a[1,2])


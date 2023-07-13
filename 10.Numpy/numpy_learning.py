import numpy

n_arr = numpy.arange(27)
print(n_arr)
print(type(n_arr))

# 1. Change the dimension of array
n_arr = n_arr.reshape(3,9)
print(n_arr)

n_arr = n_arr.reshape(3,3,3)
print(n_arr)
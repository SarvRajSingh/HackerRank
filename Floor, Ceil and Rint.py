import numpy as np
np.set_printoptions(legacy="1.13")

my_array = np.array(list(map(float, input().split())))
floored_array = np.floor(my_array)
ceiled_array = np.ceil(my_array)
rint_array = np.rint(my_array)


print(floored_array)
print(ceiled_array)
print(rint_array)

import numpy as np

n= np.array(list(map(float, input().split())))
value= float(input())

print(np.polyval(n, value))

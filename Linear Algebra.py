import numpy as np

A= []
n= int(input())
for _ in range(n):
    A.append(list(map(float, input().split())))

A= np.array(A)
print(round(np.linalg.det(A), 2))

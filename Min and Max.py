import numpy as np

n= input().split()

first_dimension= int(n[0])
second_dimension= int(n[1])


A_elements= []

for _ in range(first_dimension):
    A_elements.extend(list(map(int, input().split())))
    
A= np.array(A_elements).reshape(first_dimension, second_dimension)
B= np.min(A, axis = 1)

C= np.max(B)

print(C)

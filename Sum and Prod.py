import numpy as np

n= input().split() # here i have supposed that input will be numbers only but in practice we should take care of boundary cases as well, use try and catch


first_dimension= int(n[0])
second_dimension= int(n[1])

A_elements = []

for _ in range(first_dimension):
    A_elements.extend(list(map(int, input().split())))
    
A= np.array(A_elements).reshape(first_dimension, second_dimension)
B= np.sum(A, axis = 0)

C= np.prod(B)

print(C)


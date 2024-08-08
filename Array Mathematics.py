import numpy as np

n= input().split()


first_dimension= int(n[0])
second_dimension= int(n[1])

A_elements = []
B_elements = []

for _ in range(first_dimension):
    A_elements.extend(list(map(int, input().split())))

A= np.array(A_elements).reshape(first_dimension, second_dimension)

for _ in range(first_dimension):
    B_elements.extend(list(map(int, input().split())))

B= np.array(B_elements).reshape(first_dimension, second_dimension)

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A% B)
print(A**B)

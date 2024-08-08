import numpy as np

def arrays():
    A= np.array(list(map(int, input().split())))
    B= np.array(list(map(int, input().split())))
    
    return A, B


A, B= arrays()
print(np.inner(A, B))
print(np.outer(A, B))

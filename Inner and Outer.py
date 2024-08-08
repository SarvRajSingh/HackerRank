import numpy as np

def arrays():
    A= np.array(list(map(int, input().split())))
    B= np.array(list(map(int, input().split())))
    
    return A, B


X, Y= arrays()
print(np.inner(X, Y))
print(np.outer(X, Y))

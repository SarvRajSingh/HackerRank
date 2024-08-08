import numpy as np

def reshape_arrays():
    n = int(input())

    A_elements = []
    B_elements = []

    for _ in range(n):
        A_elements.append(list(map(int, input().split())))

    A = np.array(A_elements)

    for _ in range(n):
        B_elements.append(list(map(int, input().split())))

    B = np.array(B_elements)

    return A, B

# Call the function
A, B = reshape_arrays()

print(np.matmul(A, B))

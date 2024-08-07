cube = lambda x: x**3 
def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    series= [0, 1]
    while len(series)<n:
        series.append(series[-1]+series[-2])
    return series

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

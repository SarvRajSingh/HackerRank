from collections import deque

T= int(input())

for i in range(T):
    sides= int(input())
    block= deque(map(int, input().split()))
    flag= "Yes"
    last= float('inf')

    while block:
        
        if block[0]>=block[-1]:
            popped= block.popleft()
    
        else:
            popped= block.pop()
        if popped> last:
            flag= "No"
            break
        else:
            last= popped

    print(flag)

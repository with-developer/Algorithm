import sys

k, n = map(int, input().split())

wires = [int(sys.stdin.readline()) for i in range(k)]
start, end = 1, sorted(wires)[-1]

while start <= end:
    
    mid = (start + end) // 2  
    cnt = 0 
    for i in wires:
        cnt += i // mid
    if cnt < n:
        end = mid - 1  
    if cnt >= n:
        start = mid + 1  

print(end)
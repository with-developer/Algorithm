def minTotalTime(N, times):
    times.sort()
    
    total = 0
    currentSum = 0
    
    for time in times:
        currentSum += time
        total += currentSum
    
    return total

N = int(input())
times = list(map(int, input().split()))

print(minTotalTime(N, times))
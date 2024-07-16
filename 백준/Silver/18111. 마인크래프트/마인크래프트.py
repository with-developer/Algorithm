import sys

def minecraft(ground, N, M, B):
    heightCounts = {}
    for row in ground:
        for height in row:
            heightCounts[height] = heightCounts.get(height, 0) + 1
    
    minHeight = min(heightCounts.keys())
    maxHeight = max(heightCounts.keys())
    
    minTime = float('inf')
    finalHeight = 0
    
    for targetHeight in range(minHeight, maxHeight + 1):
        inventory = B
        time = 0
        
        for height, count in heightCounts.items():
            if height > targetHeight:
                inventory += (height - targetHeight) * count
                time += 2 * (height - targetHeight) * count
            elif height < targetHeight:
                inventory -= (targetHeight - height) * count
                time += (targetHeight - height) * count
        
        if inventory >= 0:
            if time <= minTime:
                minTime = time
                finalHeight = targetHeight
    
    return minTime, finalHeight

N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]

time, height = minecraft(ground, N, M, B)
print(time, height)
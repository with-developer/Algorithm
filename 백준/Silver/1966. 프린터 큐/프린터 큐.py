from collections import deque

def printer_queue(n, m, priorities):
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    count = 0
    
    while queue:
        current = queue.popleft()
        if any(current[1] < item[1] for item in queue):
            queue.append(current)
        else:
            count += 1
            if current[0] == m:
                return count

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))
    print(printer_queue(n, m, priorities))
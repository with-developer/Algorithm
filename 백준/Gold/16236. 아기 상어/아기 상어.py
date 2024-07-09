from sys import stdin
from collections import deque
read = stdin.readline

N = int(read())
board = [list(map(int, read().split())) for _ in range(N)]
shark = 2
shark_x, shark_y = 0, 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            shark_x, shark_y = i, j
            board[i][j] = 0
            break

def bfs(x, y):
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    q = deque([(x, y, 0)])
    eat = []
    while q:
        x, y, d = q.popleft()
        for dx, dy in (-1, 0), (0, -1), (0, 1), (1, 0):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] or board[nx][ny] > shark:
                continue
            visited[nx][ny] = 1
            q.append((nx, ny, d + 1))
            if 0 < board[nx][ny] < shark:
                eat.append((nx, ny, d + 1))
    return eat

time = 0
eat = 0

while True:
    e = bfs(shark_x, shark_y)
    if not e:
        break
    e.sort(key=lambda x: (x[2], x[0], x[1]))
    ex, ey, ed = e[0]
    board[ex][ey] = 0
    time += ed
    eat += 1
    if eat == shark:
        shark += 1
        eat = 0
    shark_x, shark_y = ex, ey
print(time)


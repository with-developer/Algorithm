from collections import deque

def dfs(graph, start, visited):
    # 현재 노드 방문 처리
    visited[start] = True
    print(start, end=' ')
    
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in sorted(graph[start]):
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    # 큐 구현을 위한 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
    print(start, end=' ')
    
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                print(i, end=' ')

# 입력 받기
n, m, v = map(int, input().split())

# 그래프 초기화
graph = [[] for _ in range(n+1)]

# 간선 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향 간선

# DFS 수행
visited = [False] * (n+1)
dfs(graph, v, visited)
print()  # 줄바꿈

# BFS 수행
visited = [False] * (n+1)
bfs(graph, v, visited)
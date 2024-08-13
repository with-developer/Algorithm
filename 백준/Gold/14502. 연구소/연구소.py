from itertools import combinations
from collections import deque
import sys
import copy

input=sys.stdin.readline

n,m=map(int,input().split())
graph=[]

for _ in range(n):
    graph.append(list(map(int,input().split())))

#빈칸을 조사하는 과정
vacant=[]

for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            vacant.append((i,j))

#빈 칸중에서 3개를 뽑는 경우를 전부 리스트로 반환
#bricks=[((0,0),(1,1),(2,2))......]
bricks=list(combinations(vacant,3))

move_x=[-1,1,0,0]
move_y=[0,0,-1,1]


def bfs(data,i,j):
    q=deque()
    q.append((i,j))

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+move_x[i],y+move_y[i]
            if 0<=nx<n and 0<=ny<m:
                if data[nx][ny]==0:
                    data[nx][ny]=2
                    q.append((nx,ny))
# 모든 가능한 경우의 수에 대해 조사
# bricks=((1,1),(2,2),(3,3))   >> t1=(1,1) t2=(2,2) ...
max_value = -1
for t1,t2,t3 in bricks:
    tmp=copy.deepcopy(graph)
    tmp[t1[0]][t1[1]],tmp[t2[0]][t2[1]],tmp[t3[0]][t3[1]]=1,1,1
    count=0
    for i in range(n):
        for j in range(m):
            if tmp[i][j]==2:
                bfs(tmp,i,j)
    for i in range(n):
        for j in range(m):
            if tmp[i][j]==0:
                count+=1

    if max_value<count:
        max_value=count


print(max_value)
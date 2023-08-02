import sys


N, M = map(int, sys.stdin.readline().split())

N_list = [i+1 for i in range(N)]
M_list = []

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    M_list.append([i,j])

#print("N_list:", N_list)
#print("M_list:", M_list)

for M_len in range(M):
    start = M_list[M_len][0]
    end = M_list[M_len][1]
    new_list = N_list[start-1: end]
    del N_list[start-1:end]
    #print(N_list)
    #print(new_list)
    new_list.reverse()
    #print(new_list)
    for idx,i in enumerate(range(start-1, end)):
        N_list.insert(i, new_list[idx])
    #print(N_list)

result = ""
for N in N_list:
    result += str(N)+" "

print(result)

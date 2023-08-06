import sys

n, m = map(int, sys.stdin.readline().split())
a_board = []; b_board = []

for i in range(n):
    if i % 2 == 0: a = ['W', 'B']; b = ['B', 'W']
    else: a = ['B', 'W']; b = ['W', 'B']
    a_board.append([a[i % 2] for i in range(m)]); b_board.append([b[i % 2] for i in range(m)])

my_board = []
for i in range(n):
    my_board.append(list(map(str, sys.stdin.readline())))

result = []
for i in range(n-7):
    for k in range(m-7):
        a_result = 0; b_result = 0
        for j in range(i,i+8):

            for s in range(k, k+8):
                if my_board[j][s] != a_board[j][s]:
                    a_result += 1
                if my_board[j][s] != b_board[j][s]:
                     b_result += 1
        result.append(a_result)
        result.append(b_result)
        
print(min(result))
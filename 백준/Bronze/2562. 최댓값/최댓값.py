n = ['0' for i in range(9)]
for i in range(9):
    n[i] = int(input())

max_num = max(n)
print(max_num)

for idx,num in enumerate(n):
    if num == max_num:
        print(idx+1)
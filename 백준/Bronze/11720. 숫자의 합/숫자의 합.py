import sys

#A, B, C = map(int, sys.stdin.readline().split())

n = int(input())

nums = input()
answer = 0

for i in nums:
    answer += int(i)

print(answer)
       
#첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.


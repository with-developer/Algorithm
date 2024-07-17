A, B, C = map(int, input().split())
D = int(input())
C += D
B += C // 60
C %= 60
A += B // 60
B %= 60
A %= 24
print(A, B, C)
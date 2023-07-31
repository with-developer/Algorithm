import sys

A, B, C = map(int, sys.stdin.readline().split())

if (A==B==C):
    #TODO: 다 똑같음
    answer = 10000 + A * 1000
elif (A==B or A==C or B==C):
    #TODO: 2개 똑같음
    if(A==B):
        answer = 1000 + A * 100
    elif(A==C):
        answer = 1000 + A * 100
    elif(B==C):
        answer = 1000 + B * 100
else:
    #TODO: 다 다름
    answer = 100 * max(A,B,C)
print(answer)
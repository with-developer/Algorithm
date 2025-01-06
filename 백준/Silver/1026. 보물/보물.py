# 배열의 크기 N 입력
N = int(input())

# 배열 A와 B 입력
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A를 오름차순으로 정렬
A.sort()

# B를 내림차순으로 정렬한 인덱스 구하기
B_indexed = [(val, idx) for idx, val in enumerate(B)]
B_indexed.sort(reverse=True)

# 결과 배열 초기화
result = [0] * N

# A의 가장 작은 값과 B의 가장 큰 값을 매칭
for i in range(N):
    result[B_indexed[i][1]] = A[i]

# S 계산
S = sum(result[i] * B[i] for i in range(N))

# 결과 출력
print(S)
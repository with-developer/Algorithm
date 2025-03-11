def find_primes(m, n):
    # 에라토스테네스의 체 알고리즘
    sieve = [True] * (n + 1)  # 모든 수를 소수로 초기화
    
    # 0과 1은 소수가 아님
    sieve[0] = sieve[1] = False
    
    # 2부터 √n까지의 수에 대해
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:  # i가 소수라면
            # i의 배수들을 모두 소수가 아닌 것으로 표시
            # i*i부터 시작 (i*2, i*3, ..., i*(i-1)은 이미 이전에 처리됨)
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    
    # m 이상 n 이하의 소수 출력
    for i in range(max(2, m), n + 1):
        if sieve[i]:
            print(i)

# 입력 받기
m, n = map(int, input().split())
find_primes(m, n)
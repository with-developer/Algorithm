def solution(n, k):
    answer = 0
    service = int(n / 10)
    n_price = n * 12000
    k_price = (k-service) * 2000
    
    answer = n_price + k_price
    return answer
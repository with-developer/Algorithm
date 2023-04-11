def solution(price, money, count):
    answer = 0
    need_price = 0
    
    for i in range(1,count+1):
        need_price += price * i
        # print("need_price: ",need_price)
    
    if (money >= need_price):
        answer = 0
        # print("have money")
        # print("nedd_price: ",need_price)
    else:
        answer = need_price - money
    
    
    return answer
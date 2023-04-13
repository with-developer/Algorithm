def solution(phone_book):
    # print("original:",phone_book)
    phone_book.sort()
    # print("sorted:",phone_book)
    
    for i in range(len(phone_book)-1):
        if (phone_book[i+1].startswith(phone_book[i])):
            return False
    
    answer = True
    return answer
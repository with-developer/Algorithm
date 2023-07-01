def solution(brown, yellow):
    answer = [0,0]
    sum = brown + yellow
    
    # 12/1 12/2 12/3 딱 떨어지는거 찾아.
    # 12:1, 12:2 12:3 12:4 12:5 12:6
    for y in range(1,sum):
        if sum % y == 0:
            x=int(sum/y)
            # print(x, y)
            if x>=y and (x-2)*(y-2)==yellow:
                # print(x,y)
                answer[0] = x
                answer[1] = y
    
    return answer

# 로직 생각
# 12는? 1:12, 2:6, 3:4

#[18, 6] -> [8, 3] (o)
#[18, 6] -> [6, 4] (x)
# 24는? 8*3은 가능한데, 6*4는 안됨
# 1,24
# 2,12
# 3, 8
# 4, 6
# 6, 4
# 8, 3
# 12,2
# 24,1


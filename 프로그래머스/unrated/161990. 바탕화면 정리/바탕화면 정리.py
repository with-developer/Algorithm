def solution(wallpaper):
    answer = []
    left = 51
    right = 0
    up = 51
    down = 0
    
    for i in range(len(wallpaper)):
        print(wallpaper[i])
        
        for j in range(len(wallpaper[i])):
            
            if wallpaper[i][j] == "#":
                
                if(left>j):
                    left = j
                if(right < j):
                    right = j
                if(up>i):
                    up = i
                if(down < i):
                    down = i

    #TODO: 제일 왼쪽에 있는 값의 위치 찾기 OK
    #TODO: 제일 위에 있는 값의 위치 찾기 OK
    #TODO: 제일 오른쪽에 있는 값의 위치 찾기 OK
    #TODO: 제일 아래에 있는 값의 위치 찾기 OK
    #print("up is",up)
    #print("left is",left)
    right = right + 1
    down = down + 1
    #print("down is",down)
    #print("right is", right)
    
    answer.append(up)
    answer.append(left)
    answer.append(down)
    answer.append(right)
    return answer
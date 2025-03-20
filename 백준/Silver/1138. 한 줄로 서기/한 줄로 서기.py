def line_up(n, info):
    # 처음에는 n개의 빈 위치가 있는 리스트를 만듭니다 (-1로 초기화)
    line = [-1] * n
    
    # 키가 작은 사람부터 큰 사람까지 차례대로 적절한 위치에 배치
    for height in range(1, n + 1):
        # 키가 height인 사람은 자신보다 키가 큰 사람이 왼쪽에 info[height-1]명 있어야 함
        bigger_count = info[height - 1]
        
        # 왼쪽에서부터 빈 위치를 찾아 bigger_count번째 빈 위치에 배치
        count = 0
        for i in range(n):
            if line[i] == -1:  # 빈 위치인 경우
                if count == bigger_count:
                    line[i] = height
                    break
                count += 1
    
    return line

def main():
    n = int(input())
    info = list(map(int, input().split()))
    result = line_up(n, info)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
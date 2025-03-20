def count_max_two_friends(graph, n):
    max_two_friends = 0
    
    for i in range(n):
        two_friends_count = 0
        
        for j in range(n):
            if i == j:
                continue  # 자기 자신은 친구가 아님
            
            # 직접 친구인 경우
            if graph[i][j] == 'Y':
                two_friends_count += 1
                continue
            
            # 공통 친구가 있는 경우
            for k in range(n):
                if graph[i][k] == 'Y' and graph[k][j] == 'Y':
                    two_friends_count += 1
                    break
        
        max_two_friends = max(max_two_friends, two_friends_count)
    
    return max_two_friends

def main():
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(input())
    
    result = count_max_two_friends(graph, n)
    print(result)

if __name__ == "__main__":
    main()
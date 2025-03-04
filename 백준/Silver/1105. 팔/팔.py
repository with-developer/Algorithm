def solve(L, R):
    """
    L과 R 사이에 있는 숫자 중 8이 가장 적게 포함된 숫자의 8 개수 계산
    """
    # 초기값 설정: 최대 가능한 값을 설정
    min_8_count = float('inf')
    
    # 범위가 충분히 좁으면 완전 탐색
    if R - L <= 100:
        for num in range(L, R + 1):
            count = str(num).count('8')
            min_8_count = min(min_8_count, count)
        return min_8_count
    
    # L과 R이 같으면 해당 숫자만 확인
    if L == R:
        return str(L).count('8')
    
    # 다음 전략: 특정 패턴의 숫자들을 먼저 검사
    
    # 1. 범위 내에서 자릿수가 바뀌는 지점 확인 (예: 99 -> 100)
    len_L, len_R = len(str(L)), len(str(R))
    
    # 자릿수가 다르면, 자릿수가 바뀌는 지점에서 8이 없는 숫자를 찾을 확률이 높음
    if len_L < len_R:
        # 각 자릿수의 첫번째 숫자와 마지막 숫자 확인
        for digits in range(len_L, len_R + 1):
            # 첫번째 숫자 (1000, 10000 등)
            if digits > 1:
                first_num = 10 ** (digits - 1)
                if L <= first_num <= R and '8' not in str(first_num):
                    return 0
            
            # 마지막 숫자 (999, 9999 등)
            if digits < len_R:
                last_num = 10 ** digits - 1
                if L <= last_num <= R and '8' not in str(last_num):
                    return 0
    
    # 2. L 근처와 R 근처의 숫자들 확인 (가장 가능성 높은 위치)
    # L 근처
    for i in range(L, min(L + 1000, R + 1)):
        count = str(i).count('8')
        min_8_count = min(min_8_count, count)
        if min_8_count == 0:
            return 0
    
    # R 근처
    for i in range(max(R - 1000, L), R + 1):
        count = str(i).count('8')
        min_8_count = min(min_8_count, count)
        if min_8_count == 0:
            return 0
    
    # 3. 각 자릿수에서 8이 아닌 숫자로만 이루어진 특수한 케이스 확인
    # 예: L=1000, R=9999인 경우 1999, 2999, 3999 등을 확인
    
    # 자릿수가 같은 경우
    if len_L == len_R:
        # 첫 자리부터 채워가며 8이 없는 숫자 구성 시도
        str_L, str_R = str(L), str(R)
        
        def backtrack(index, curr_num):
            if index == len_L:
                # 조건을 만족하는 숫자 완성
                if L <= int(curr_num) <= R:
                    return 0  # 8이 없는 숫자 생성 성공
                return float('inf')
            
            min_count = float('inf')
            start_digit = int(str_L[index]) if curr_num == str_L[:index] else 0
            end_digit = int(str_R[index]) if curr_num == str_R[:index] else 9
            
            for digit in range(start_digit, end_digit + 1):
                if digit != 8:
                    count = backtrack(index + 1, curr_num + str(digit))
                    min_count = min(min_count, count)
                    if min_count == 0:
                        return 0
            
            return min_count
        
        result = backtrack(0, "")
        if result == 0:
            return 0
    
    # 4. 특정 자리에 8이 강제로 나타나는지 확인
    if len_L == len_R:
        str_L, str_R = str(L), str(R)
        forced_8_count = 0
        
        # 자릿수가 같은 경우, 각 자리가 모두 8인지 확인
        for i in range(len_L):
            if str_L[:i] != str_R[:i]:
                break  # 이전 자리가 달라지면 더 이상 강제로 8일 필요가 없음
            
            # 현재 자리가 L과 R 모두에서 8인 경우, 이 자리는 항상 8
            if str_L[i] == '8' and str_R[i] == '8':
                forced_8_count += 1
        
        if forced_8_count > 0:
            return forced_8_count
    
    # 여기까지 왔으면 8이 없는 숫자를 찾지 못했거나 특정 자리에 8이 강제되지 않음
    # 대부분의 경우 최소 개수는 1일 가능성이 높음
    return min_8_count if min_8_count != float('inf') else 1

# 입력 처리
L, R = map(int, input().split())
print(solve(L, R))
def solve_scenario(scenario_number, n):
    # 여학생 이름 저장
    names = []
    for i in range(n):
        names.append(input())
    
    # 각 여학생별 귀걸이 처리 횟수 추적
    counts = [0] * n
    
    # 압수 및 반환 기록 처리
    for _ in range(2*n - 1):
        student_id, earring_type = input().split()
        student_id = int(student_id) - 1  # 0-based 인덱스로 변환
        
        # 처리 횟수 증가
        counts[student_id] += 1
    
    # 홀수 횟수 처리된 여학생 찾기 (압수만 되고 반환되지 않은 경우)
    for i in range(n):
        if counts[i] % 2 == 1:
            print(f"{scenario_number} {names[i]}")
            break

# 시나리오 처리
scenario_number = 1
while True:
    line = input()
    if line == "0":
        break
    
    n = int(line)
    solve_scenario(scenario_number, n)
    scenario_number += 1
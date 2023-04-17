# 💻 프로그래머스 알고리즘 공부 💻

프로그래머스 정답률 순으로 푸는 중입니다. (Level 0 제외)<br>
사용 언어: Python<br><br>
목표: 4월 10 ~ 14일 60 문제 풀기<br><br>
4월 10일: 20문제 풀이 완료<br>
4월 11일: 15문제 풀이 완료<br>
4월 12일: 9문제 풀이 완료<br>
4월 13일: 6문제 풀이 완료<br>
4월 14일: 2문제 풀이 완료<br>
총 52문제 풀었습니다.<br><br>
코딩 테스트는 끝났지만, 시간 날때마다 문제 풀이 업로드중입니다.




# 기억해야 할 것
1. math.pow(number,2): number의 2제곱을 리턴
2. math.sqrt(number): number의 제곱근을 리턴
3. map(function, iterable): 반복 가능한 iterable을 첫번째 인자로 넣어서 함수를 실행
4. ''.join(list): 리스트 내용을 합쳐서 문자열로 변환
5. chr(정수), ord("문자"): ascii 문자, code를 출력
6. N * M 크기의 2차원 리스트 초기화
```python
n = 4
m = 3
array = [[0] * m for _ in range(n)]
print("result: ",array)

result: [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
```
7. 문장 중 첫 단어들만 대문자로 변경
```python
s = "hello  python"
answer = ''
s=s.split(' ') 
    
for i in range(len(s)):
    s[i]=s[i].capitalize() #캐피탈라이즈 함수 쓰면 단어의 첫 글자만 대문자로 변경하고, 나머지는 소문자로 반환해줌.
answer=' '.join(s)
return answer
```
7. math.gcd(n,m): n과 m의 최대공약수
8. math.lcm(n,m): n과 m의 최소공배수 -> python 3.9부터 사용 가능하며, 업데이트가 되지 않았을땐 "n*m/최대공약수"로 계산하면됨
9. format 진수 변환 (10진수를 2,8,16 진수로 변환)
```python
format(10,'b') # 10을 2진수로
format(10,'o') # 10을 8진수로
format(10,'x') # 10을 16진수로
```
10. int 진수 변환(n진수를 10진수로 변환)
```python
int('10',3) # 3진수의 10을 int로 변환
```


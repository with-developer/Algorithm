# 💻 프로그래머스 & 백준 알고리즘 공부 💻


사용 언어: Python<br><br>



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
8. math.lcm(n,m): n과 m의 최소공배수
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


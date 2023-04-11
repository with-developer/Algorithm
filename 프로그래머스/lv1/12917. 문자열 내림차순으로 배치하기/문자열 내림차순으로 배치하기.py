def solution(s):
    result = []
    answer = ''
    for i in range(len(s)):
        result.append(ord(s[i]))

    result.sort()
    result.reverse()

    for i in range(len(s)):
        answer += chr(result[i])

    return answer
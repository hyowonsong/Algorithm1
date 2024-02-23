def solution(s):
    answer = 0
    if s[0] == '0':
        return false
    else:
        s = int(s)
        answer += s
    return answer
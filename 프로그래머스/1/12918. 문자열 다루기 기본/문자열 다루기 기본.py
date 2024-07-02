# 문자열 다루기 기본
# 문자열의 길이기 4혹은 6이고 숫자로만 구성

def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True
    else:
        return False
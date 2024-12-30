# 1. 각 문자열의 n 번째 글자를 기준으로 오름차순 정렬

def solution(strings, n):
    # n번째 문자를 기준으로 정렬, n번째 문자가 같으면 사전순으로 자동 정렬
    return sorted(strings, key=lambda string: (string[n], string))

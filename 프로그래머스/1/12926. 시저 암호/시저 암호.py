def solution(s, n):
    low = "abcdefghijklmnopqrstuvwxyz" # 소문자. 인덱스는 0에서 25
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = ''
    for char in s:
        # 만약 소문자 이면
        if char in low:
            ind = low.find(char)+n
            answer += low[ind%26]
        # 만약 대문자 이면
        elif char in up:
            ind = up.find(char)+n
            answer += up[ind%26]
        # 공백이라면
        else:
            answer += " "
    return answer
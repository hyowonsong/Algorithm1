# 덧칠하기

def solution(n, m, section):
    answer = 1 # 칠하는 횟수
    paint = section[0] # 덧칠 시작점
    for i in range(1, len(section)):
        if section[i] - paint >= m:
            answer += 1
            paint = section[i]       # i로 초기해줘야 덧칠 시작점이 바뀌지
            
    return answer
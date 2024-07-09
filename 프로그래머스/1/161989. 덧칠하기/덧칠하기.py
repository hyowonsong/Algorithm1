# 덧칠하기

def solution(n, m, section):
    answer = 1 # 칠하는 횟수
    # 덧칠 시작점 맨처음에 정의해줘야(나중에 초기화 정의함)
    paint = section[0] 
    # section의 길이만큼 for 문 돌아야
    for i in range(1, len(section)):
        if section[i] - paint >= m:
            answer += 1
            paint = section[i]       # i로 초기해줘야 덧칠 시작점이 바뀌지
            
    return answer
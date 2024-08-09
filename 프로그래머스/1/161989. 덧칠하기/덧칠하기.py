# 덧칠하기

def solution(n, m, section):
    answer = 1 # 칠하는 횟수(맨처음 1로 설정)
    # 덧칠 시작점 맨처음에 정의해줘야(나중에 초기화 정의함)
    paint = section[0] 
    # section의 길이만큼 for 문 돌아야(1부터)
    for i in range(1, len(section)):
        if section[i] - paint >= m:
            # 더 크다면 그냥 answer += 1 해준다. 다른 계산X
            answer += 1
            # i로 초기해줘야 덧칠 시작점이 바뀌지 안그러면 계속 section[0]
            paint = section[i]  
        else:
            continue
            
    return answer
# 덧칠하기 - 핵심은 페인트 칠해야하는 곳이 롤러 m보다 크면 +1

def solution(n, m, section):
    answer = 1 # 칠하는 횟수(맨처음 1로 설정)
    # 덧칠 시작점 맨처음에 정의해줘야(나중에 초기화 정의함)
    paint = section[0] 
    
    # section[0] 같은 경우 먼저 정의 했으니까 1부터 시작
    for i in range(1, len(section)):
        if section[i] - paint >= m:
            answer += 1
            # i로 초기해줘야 덧칠 시작점이 바뀌지 안그러면 계속 section[0]
            paint = section[i]  
        else:
            continue
            
    return answer
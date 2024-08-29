def solution(n, stations, w):
    answer = 0    
    # 현재 검사 중인 아파트 위치
    start = 1    
    # 현재 확인 중인 기존 기지국의 인덱스
    index = 0       

    while start <= n:  # 모든 아파트를 검사할 때까지 반복
        # 현재 기지국의 위치가 기존 기지국의 범위 안에 있고
        # 현재 검사중인 아파트 위치가 기지국의 신호 범위 내에 있으면
        if index < len(stations) and start >= stations[index] - w:
            # 그 기지국의 범위를 넘어서 다음 위치로 이동하고
            # 다음 기존 기지국으로 이동
            start = stations[index] + w + 1
            index += 1  
        else:
            # 기존 기지국의 범위 밖이라면, 새 기지국 설치
            answer += 1
            # 새로 설치한 기지국의 신호 범위 끝 바로 다음 위치로 이동
            start += 2 * w + 1

    return answer  

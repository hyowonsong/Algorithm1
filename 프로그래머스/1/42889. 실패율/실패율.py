# 실패율

def solution(N, stages):
    # 각 스테이지에 도달한 플레이어 수를 저장할 리스트
    stages_count = [0]*(N+2)
    
    # 스테이지 별로 사용자 수 계산(stage에 2라고 적혀있으면 2번 스테이지에 추가)
    for stage in stages:
        stages_count[stage] += 1
    
    # 총 사용자 수
    total_players = len(stages)

    # 실패율 계산
    failure_rates = []
    for i in range(1, N+1):
        # 해당 스테이지에 도달한 사용자가 없는 경우
        if total_players == 0:
            failure_rate = 0
        else:
            failure_rate = stages_count[i]/total_players

        failure_rates.append((i, failure_rate))
        # 다음 스테이지로 진행할 사용자 수 감소
        total_players -= stages_count[i]
    
    # 실패율 기준 내림차순 정렬 (실패율이 같으면 스테이지 번호 오름차순)
    # -를 붙이면 내림차순 정렬이 된다. 
    failure_rates.sort(key = lambda x: (-x[1], x[0]) )

    # 정렬된 스테이지 번호만 추출
    result = []
    for i in failure_rates:
        result.append(i[0])

    return result
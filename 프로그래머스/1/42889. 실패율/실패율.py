def solution(N, stages):
    # 각 스테이지별 실패율을 저장할 리스트
    failure_rates = []
    
    # 전체 사용자 수
    total_users = len(stages)
    
    # 각 스테이지에 대한 실패율 계산
    for i in range(1, N + 1):
        # 현재 스테이지에 도달한 사용자 수
        users_on_stage = stages.count(i)
        
        # 실패율 계산
        if total_users > 0:
            failure_rate = users_on_stage / total_users
        else:
            failure_rate = 0
        
        # 실패율과 스테이지 번호를 튜플로 저장
        failure_rates.append((i, failure_rate))
        
        # 전체 사용자 수 갱신: 현재 스테이지에 도전한 사용자는 제외
        total_users -= users_on_stage
    
    # 실패율을 기준으로 내림차순 정렬, 실패율이 같으면 스테이지 번호 기준 오름차순 정렬
    failure_rates.sort(key=lambda x: (-x[1], x[0]))
    
    # 결과에서 스테이지 번호만 추출
    result = []
    for item in failure_rates:
        result.append(item[0])
    
    return result
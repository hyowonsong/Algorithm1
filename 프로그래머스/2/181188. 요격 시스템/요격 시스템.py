def solution(targets):
    # 미사일을 종료 지점(e) 기준으로 정렬
    targets.sort(key=lambda x: x[1])
    
    # 현재까지의 요격 미사일 수
    interceptors = 0
    # 마지막 요격 지점
    last_intercept = -1
    
    for start, end in targets:
        # 현재 미사일이 마지막 요격 지점보다 뒤에서 시작하면
        # 새로운 요격 미사일이 필요
        if start >= last_intercept:
            interceptors += 1
            # 새로운 요격 지점을 현재 미사일의 종료 지점 직전으로 설정
            last_intercept = end
            
    return interceptors
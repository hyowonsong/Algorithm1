def point(route):
    return route[1]

def solution(routes):
    # 나간 지점을 기준으로 정렬
    routes.sort(key=point)  
    # 카메라 위치 초기화 (가장 작은 진입/나간 지점보다 작은 값)
    camera = -30001  
    # 설치된 카메라 수
    count = 0  

    for route in routes:
        # 현재 카메라가 해당 차량의 진입 지점보다 앞에 있으면
        if camera < route[0]: 
            # 해당 차량의 나간 지점에 새 카메라 설치
            camera = route[1]  
            count += 1

    return count
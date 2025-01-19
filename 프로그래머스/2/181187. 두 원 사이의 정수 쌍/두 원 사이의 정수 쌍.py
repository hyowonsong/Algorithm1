import math

def solution(r1, r2):
    count = 0  # 총 점 개수

    for x in range(1, r2 + 1):  # x 좌표를 순회
        # 작은 원의 바깥쪽 y 시작점
        if x < r1:
            y_min = math.ceil(math.sqrt(r1**2 - x**2))
        else:
            y_min = 0
        
        # 큰 원의 안쪽 y 끝점
        y_max = math.floor(math.sqrt(r2**2 - x**2))
        
        # 가능한 y 값의 개수를 더함
        count += (y_max - y_min + 1)
    
    return count * 4  # 전체 대칭성 반영

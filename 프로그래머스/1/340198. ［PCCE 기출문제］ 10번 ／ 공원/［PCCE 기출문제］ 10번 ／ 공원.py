def solution(mats, park):
    n = len(park)
    m = len(park[0])
    
    # 큰 크기부터 확인하기 위해 정렬
    mats.sort(reverse=True)
    
    for size in mats:
        # 모든 가능한 시작 위치 확인
        for i in range(n):
            for j in range(m):
                # 범위를 벗어나면 다음 위치 확인
                if i + size > n or j + size > m:
                    continue
                    
                # 해당 영역에 사람이 있는지 확인
                can_place = True
                for x in range(i, i + size):
                    for y in range(j, j + size):
                        if park[x][y] != "-1":
                            can_place = False
                            break
                    if not can_place:
                        break
                
                # 돗자리를 놓을 수 있는 공간을 찾았다면 현재 크기 반환
                if can_place:
                    return size
    
    return -1
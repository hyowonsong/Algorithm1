def solution(wallpaper):
    # 파일 위치의 최소/최대 좌표를 저장할 변수 초기화
    min_x, min_y = float('inf'), float('inf')
    max_x, max_y = -1, -1
    
    # wallpaper를 순회하면서 파일("#")의 위치 확인
    for i, row in enumerate(wallpaper):
        for j, cell in enumerate(row):
            if cell == "#":
                # 파일 위치의 최소/최대 좌표 업데이트
                min_x = min(min_x, i)
                min_y = min(min_y, j)
                max_x = max(max_x, i)
                max_y = max(max_y, j)
    
    # 드래그의 시작점과 끝점 결정
    # 주의: 끝점은 파일을 포함해야 하므로 각각 +1을 해줍니다.
    return [min_x, min_y, max_x + 1, max_y + 1]
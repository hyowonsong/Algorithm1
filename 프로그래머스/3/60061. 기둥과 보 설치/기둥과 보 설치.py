
def check_pillar(x, y, structures):
    # 기둥이 설치 가능한지 확인하는 함수
    # x, y: 설치할 좌표
    # structures: 현재 설치된 구조물들의 목록 [[x, y, a], ...]

    # 바닥이면 설치 가능
    if y == 0:
        return True
    
    # 다른 기둥 위면 설치 가능
    if [x, y-1, 0] in structures:
        return True
    
    # 보의 한쪽 끝부분 위면 설치 가능
    if [x-1, y, 1] in structures or [x, y, 1] in structures:
        return True
        
    return False

def check_beam(x, y, structures):
    # 보가 설치 가능한지 확인하는 함수
    # x, y: 설치할 좌표
    # structures: 현재 설치된 구조물들의 목록 [[x, y, a], ...]

    # 한쪽 끝부분이 기둥 위면 설치 가능
    if [x, y-1, 0] in structures or [x+1, y-1, 0] in structures:
        return True
    
    # 양쪽 끝부분이 다른 보와 동시에 연결되어 있으면 설치 가능
    if [x-1, y, 1] in structures and [x+1, y, 1] in structures:
        return True
        
    return False

def can_delete(x, y, a, structures):
    # 구조물을 삭제할 수 있는지 확인하는 함수
    # x, y: 삭제할 좌표, # a: 구조물의 종류 (0: 기둥, 1: 보)
    # structures: 현재 설치된 구조물들의 목록
    # 일단 해당 구조물을 삭제
    structures.remove([x, y, a])
    
    # 남은 구조물들이 조건을 만족하는지 확인
    for structure in structures:
        curr_x, curr_y, curr_a = structure
        
        # 기둥인 경우
        if curr_a == 0:
            if not check_pillar(curr_x, curr_y, structures):
                structures.append([x, y, a])
                return False
        # 보인 경우
        else:
            if not check_beam(curr_x, curr_y, structures):
                structures.append([x, y, a])
                return False
                
    # 삭제된 상태에서 모든 구조물이 조건을 만족하면 삭제 가능
    structures.append([x, y, a])
    return True

def solution(n, build_frame):
    # n: 벽면의 크기
    # build_frame: 작업 순서가 담긴 2차원 배열 [[x, y, a, b], ...]
    # a: 구조물의 종류 (0: 기둥, 1: 보)
    # b: 작업 종류 (0: 삭제, 1: 설치)
    structures = []
    
    for x, y, a, b in build_frame:
        # 설치하는 경우 (b == 1)
        if b == 1:
            # 일단 구조물 설치
            structures.append([x, y, a])
            
            # 설치 가능한지 확인
            is_possible = True
            if a == 0:  # 기둥
                if not check_pillar(x, y, structures):
                    is_possible = False
            else:  # 보
                if not check_beam(x, y, structures):
                    is_possible = False
            
            # 설치가 불가능하면 제거
            if not is_possible:
                structures.remove([x, y, a])
                
        # 삭제하는 경우 (b == 0)
        else:
            if can_delete(x, y, a, structures):
                structures.remove([x, y, a])
    
    # x좌표 기준 오름차순, x좌표가 같으면 y좌표 기준 오름차순, 
    # y좌표가 같으면 기둥(0)이 보(1)보다 앞에 오도록 정렬
    return sorted(structures, key=lambda x: (x[0], x[1], x[2]))
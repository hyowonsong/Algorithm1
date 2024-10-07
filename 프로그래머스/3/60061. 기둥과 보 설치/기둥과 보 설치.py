# 기둥을 설치할 수 있는지 확인하는 함수
def can_build_pillar(x, y, structure):
    # 기둥이 바닥 위에 있으면 설치 가능
    if y == 0:
        return True
    # 기둥 아래에 다른 기둥이 있으면 설치 가능
    if [x, y-1, 0] in structure:
        return True
    # 기둥이 보의 끝 부분 위에 있으면 설치 가능
    if [x-1, y, 1] in structure or [x, y, 1] in structure:
        return True
    # 어떤 조건도 만족하지 않으면 설치 불가
    return False

# 보를 설치할 수 있는지 확인하는 함수
def can_build_beam(x, y, structure):
    # 보의 한쪽 끝이 기둥 위에 있으면 설치 가능
    if [x, y-1, 0] in structure or [x+1, y-1, 0] in structure:
        return True
    # 보의 양쪽 끝이 다른 보와 연결되어 있으면 설치 가능
    if [x-1, y, 1] in structure and [x+1, y, 1] in structure:
        return True
    # 어떤 조건도 만족하지 않으면 설치 불가
    return False

# 구조물이 올바른지 확인하는 함수
def is_valid_structure(structure):
    for x, y, a in structure:
        # 기둥일 경우
        if a == 0:
            if not can_build_pillar(x, y, structure):
                return False
        # 보일 경우
        elif a == 1:
            if not can_build_beam(x, y, structure):
                return False
    return True

def solution(n, build_frame):
    structure = []  # 현재 구조물 상태를 저장할 리스트

    # 명령어를 하나씩 처리
    for x, y, a, b in build_frame:
        if b == 1:  # 설치 명령일 경우
            structure.append([x, y, a])  # 기둥 또는 보를 설치
            if not is_valid_structure(structure):  # 설치 후 구조물이 조건을 만족하지 않으면
                structure.remove([x, y, a])  # 다시 설치 취소
        elif b == 0:  # 삭제 명령일 경우
            structure.remove([x, y, a])  # 기둥 또는 보를 삭제
            if not is_valid_structure(structure):  # 삭제 후 구조물이 조건을 만족하지 않으면
                structure.append([x, y, a])  # 다시 삭제 취소

    # 결과 정렬
    structure.sort(key=lambda x: (x[0], x[1], x[2]))
    return structure

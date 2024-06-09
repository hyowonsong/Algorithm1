def match(arr, key, rot, r, c):
    n = len(key)
    for i in range(n):
        for j in range(n):
            if rot == 0:  # 만약 회전이 없다면, 키를 그대로 더합니다
                arr[r + i][c + j] += key[i][j]
            elif rot == 1:
                arr[r + i][c + j] += key[n - 1 - j][i]  # 90도 회전
            elif rot == 2:
                arr[r + i][c + j] += key[n - 1 - i][n - 1 - j]  # 180도 회전
            else:
                arr[r + i][c + j] += key[j][n - 1 - i]  # 270도 회전

def check(arr, offset, n):
    for i in range(n):
        for j in range(n):
            if arr[offset + i][offset + j] != 1:
                return False  # 자물쇠 부분 중 하나라도 맞지 않으면 False 반환
    return True  # 모든 부분이 1로 맞다면 True 반환

def solution(key, lock):
    offset = len(key) - 1
    # 자물쇠를 (1,1)에서 떨어지게 놔두는데 그 거리 만큼을 offset이라고 한다

    # 행, 열의 좌표를 r, c로 설정하고 범위는 offset + 자물쇠 길이
    for r in range(offset + len(lock)):
        for c in range(offset + len(lock)):
            # 열쇠를 돌려보는 것(4개 방향으로 돌린다.)
            for rot in range(4):
                # 2차원 배열 초기값을 설정합니다.
                arr = [[0 for _ in range(58)] for _ in range(58)]

                # 자물쇠를 복사해줍니다.
                for i in range(len(lock)):
                    for j in range(len(lock)):
                        arr[offset + i][offset + j] = lock[i][j]

                match(arr, key, rot, r, c)
                # 만약 check 함수가 True를 반환하면 열쇠가 맞아떨어진 경우이므로 True 반환
                if check(arr, offset, len(lock)):
                    return True

    return False  # 모든 경우를 확인해도 맞는 열쇠를 찾을 수 없으면 False 반환

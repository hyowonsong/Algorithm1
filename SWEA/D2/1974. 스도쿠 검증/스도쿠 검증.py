
T = int(input())

def is_valid(graph):
    # 가로, 세로, 3x3 격자 체크를 위한 배열
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            num = graph[i][j]
            if num < 1 or num > 9:
                return 0
            
            # 행 검증
            if num in rows[i]:
                return 0
            rows[i].add(num)

            # 열 검증
            if num in cols[j]:
                return 0
            cols[j].add(num)

            # 3x3 박스 검증
            box_index = (i // 3) * 3 + (j // 3)
            if num in boxes[box_index]:
                return 0
            boxes[box_index].add(num)

    return 1


for t in range(1, T+1):
    graph = [list(map(int,input().split())) for _ in range(9)]

    # 스도쿠 검증
    result = is_valid(graph)

    print(f'#{t} {result}')
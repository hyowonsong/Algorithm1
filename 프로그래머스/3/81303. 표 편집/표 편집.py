def solution(n, k, cmd):
    # 링크드 리스트 초기화 
    linked_list = {}
    for i in range(n):
        if i == 0:  # 첫 번째 행
            linked_list[i] = [None, i + 1]
        elif i == n - 1:  # 마지막 행
            linked_list[i] = [i - 1, None]
        else:  # 중간 행
            linked_list[i] = [i - 1, i + 1]
    
    # 삭제된 행을 저장할 스택
    stack = []
    current = k
    
    for command in cmd:
        parts = command.split()
        if parts[0] == "U":  # 위로 이동
            steps = int(parts[1])
            for _ in range(steps):
                current = linked_list[current][0]
        elif parts[0] == "D":  # 아래로 이동
            steps = int(parts[1])
            for _ in range(steps):
                current = linked_list[current][1]
        elif parts[0] == "C":  # 삭제
            prev, next_ = linked_list[current]
            stack.append((current, prev, next_))  # 현재 상태 스택에 저장
            if prev is not None:
                linked_list[prev][1] = next_
            if next_ is not None:
                linked_list[next_][0] = prev
            # 현재 행 변경
            current = next_ if next_ is not None else prev
        elif parts[0] == "Z":  # 복구
            node, prev, next_ = stack.pop()
            if prev is not None:
                linked_list[prev][1] = node
            if next_ is not None:
                linked_list[next_][0] = node
    
    # 최종 결과 계산
    result = ["O"] * n
    while stack:
        node, _, _ = stack.pop()
        result[node] = "X"
    
    return "".join(result)
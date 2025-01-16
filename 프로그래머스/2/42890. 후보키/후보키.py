def solution(relation):
    n = len(relation)  
    m = len(relation[0]) 
    candidate_keys = []

    # 모든 부분 집합 탐색 (비트마스크 활용)
    for subset in range(1, 1 << m):  # 1부터 2^m - 1까지
        # 유일성 확인
        seen = set()
        for row in relation:
            key = tuple(row[col] for col in range(m) if subset & (1 << col))
            seen.add(key)
        if len(seen) == n:  # 유일성을 만족하면
            # 최소성 확인
            is_minimal = True
            for candidate in candidate_keys:
                if candidate & subset == candidate:  # 후보키가 현재 조합의 부분 집합인지 확인
                    is_minimal = False
                    break
            if is_minimal:
                candidate_keys.append(subset)
    
    return len(candidate_keys)

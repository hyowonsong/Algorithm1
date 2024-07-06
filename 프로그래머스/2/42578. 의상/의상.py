def solution(clothes):
    answer = 0
    hash_map ={}
    for clothe, type in clothes:
        # 키에 해당하는 값이 존재하면 그 값을 반환, 존재하지 않으면 기본값으로 0을 반환
        hash_map[type] = hash_map.get(type, 0) + 1

    
    answer = 1
    # 여기서 입지 않는 경우를 추가해서 모든 조합 계산했어야
    for type in hash_map:
        answer *= hash_map[type] + 1
    return answer - 1
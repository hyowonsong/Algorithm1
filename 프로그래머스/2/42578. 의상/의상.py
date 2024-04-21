# 의상

def solution(clothes):
    answer = 0 
    hash_map = {}
    for clothe, type in clothes:
        # 해시 맵에서 type에 아무것도 없으면 0해주고 +1
        hash_map[type] = hash_map.get(type, 0) + 1

    
    answer = 1
    # 여기서 입지 않는 경우를 추가해서 모든 조합 계산했어야
    for type in hash_map:
        answer *= hash_map[type] + 1
    return answer - 1
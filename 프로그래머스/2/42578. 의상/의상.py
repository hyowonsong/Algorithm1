# 의상

def solution(clothes):
    # 의상 종류별로 갯수를 세기 위한 딕셔너리 생성
    clothes_count = {}
    
    # clothes 배열 순회하며 딕셔너리에 카운트 저장
    for clothe, type in clothes:
        if type in clothes_count:
            clothes_count[type] += 1
        else:
            clothes_count[type] = 1
    
    # 각 종류별 의상 갯수 + 1 (아무것도 입지 않은 경우를 체크)
    combinations = 1
    for count in clothes_count.values():
        combinations *= (count + 1)
    
    # 최소 하나는 입어야 하므로, 모두 선택하지 않는 경우를 뺌
    return combinations - 1

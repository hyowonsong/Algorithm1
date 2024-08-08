# 의상

def solution(clothes):
    answer = 0
    hash_map = {}

    # 의상의 이름, 의상의 종류로 이루어짐
    for clothe,type in clothes:
        # hash_map.get(key, default)
        # default는 키가 딕셔너리에 없을 때 반환하는 기본 값
        hash_map[type] = hash_map.get(type,0) + 1

    answer = 1
    for type in hash_map:
        answer *= hash_map[type] + 1

    # 모든 조합을 계산하고 아무것도 입지 않는 경우는 제외해야 하므로 최종 결과에서 1 빼기
    return answer-1
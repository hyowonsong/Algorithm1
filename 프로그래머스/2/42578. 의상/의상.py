# 의상(해시맵을 사용한다는 것을 체크!)

def solution(clothes):
    #  옷을 종류별로 구분하기
    hash_map = {}
    for clothe, type in clothes:
        hash_map[type] = hash_map.get(type, 0) + 1
        
    #  입지 않는 경우를 추가하여 모든 조합 계산하기
    answer = 1
    for type in hash_map:   
        answer *= (hash_map[type] + 1)
    
    #  아무종류의 옷도 입지 않는 경우 제외하기
    return answer - 1
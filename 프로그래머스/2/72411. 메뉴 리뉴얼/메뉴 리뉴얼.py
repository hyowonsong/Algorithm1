# 메뉴 리뉴얼

# 단품 메뉴를 코스요리 형태로 재구성
# 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성

from itertools import combinations
from collections import Counter

# orders는 손님들의 주문 목록을 나타내며, 
# course는 새로 만들고자 하는 코스 요리의 각 메뉴 수
def solution(orders, course):
    answer = []

    # course 배열에 있는 코스요리 메뉴 수에 대해 반복
    for c in course:
        # 조합의 빈도를 저장할 Counter 객체 생성
        comb_counter = Counter()
        
        
        # 각 손님의 주문(order)을 알파벳 순서로 정렬
        # 이렇게 하면 'ABC'와 'CBA' 같은 다른 순서의 같은 조합을 하나로 통일
        for order in orders:
            # 정렬된 주문으로부터 길이가 c인 모든 조합 생성 및 빈도 카운트
            sorted_order = sorted(order)
            comb_counter.update(combinations(sorted_order, c))

        # comb_counter가 비어 있지 않다면,
        if comb_counter: 
        # 가장 많이 주문된 조합의 횟수를 max_count에 저장
            max_count = max(comb_counter.values())
            # max_count가 1보다 큰 경우(즉, 두 번 이상 주문된 경우)에만 계속 진행
            if max_count > 1:
                # 각 조합과 그 조합의 주문 횟수에 대해 반복(items는 (키,값)) 쌍을 반환
                for combo, values in comb_counter.items():
                    # 조합의 주문 횟수가 최대 주문 횟수와 같은 경우 결과에 추가
                    if values == max_count:
                        answer.append(''.join(combo))  # 조합을 문자열로 변환하여 추가

    answer.sort()  # 최종 결과를 사전순으로 정렬
    
    return answer  # 정렬된 결과 반환
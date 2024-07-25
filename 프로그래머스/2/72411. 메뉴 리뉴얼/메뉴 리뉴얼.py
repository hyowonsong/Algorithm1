from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    # course 배열에 있는 코스요리 메뉴 수에 대해 반복
    for c in course:
        comb_counter = Counter()  # 조합의 빈도를 저장할 Counter 객체 생성
        
        # 각 손님의 주문에 대해 처리
        for order in orders:
            sorted_order = sorted(order)  # 메뉴를 알파벳 순서로 정렬
            # 정렬된 주문으로부터 길이가 c인 모든 조합 생성 및 빈도 카운트
            comb_counter.update(combinations(sorted_order, c))

        # 조합 중 가장 많이 함께 주문된 횟수 찾기
        if comb_counter:
            max_count = max(comb_counter.values())  # 가장 많이 주문된 횟수 찾기
            # 가장 많이 주문된 횟수가 1보다 큰 경우만 고려
            if max_count > 1:
                # 각 조합과 그 조합의 주문 횟수에 대해 반복
                for combo, count in comb_counter.items():
                    # 조합의 주문 횟수가 최대 주문 횟수와 같은 경우 결과에 추가
                    if count == max_count:
                        answer.append(''.join(combo))  # 조합을 문자열로 변환하여 추가

    answer.sort()  # 최종 결과를 사전순으로 정렬
    
    return answer  # 정렬된 결과 반환
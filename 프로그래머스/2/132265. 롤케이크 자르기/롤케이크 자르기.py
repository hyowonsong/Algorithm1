# 롤케이크 자르기

from collections import Counter


def solution(topping):
    answer = 0
    # 먼저 철수가 모든 토핑을 가져가고 동생은 아무것도 가져 가지 않은 상태로 초기화
    chulsu = Counter(topping)
    brother = set()

    
    for t in topping:
        # 철수가 동생에게 하나씩 주면서 서로 가진 토핑의 개수가 일치하면 answer을 +=1 증감
        chulsu[t] -= 1
        brother.add(t)

        # 철수가 가지고 있는 토핑의 개수가 0개라면 해당 토핑을 지워줍니다. 
        if chulsu[t] == 0:
            chulsu.pop(t)

        if len(chulsu) == len(brother):
            answer += 1

    return answer
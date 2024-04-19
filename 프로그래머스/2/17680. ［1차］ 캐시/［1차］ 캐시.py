# LRU 알고리즘은 스택을 사용하는 것이 적절하지 않다. 링크드리스트나 deque를 사용해야 한다.

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen = cacheSize) # maxlen은 deque에 의해 유지되는 요소의 최대 길이를 나타내는 매개변수

    for city in cities:
        city_lower = city.lower()  # 대소문자 구분하지 않기 위해 소문자로 변환
        
        if city_lower in cache:  # cache hit
            cache.remove(city_lower)  # 해당 도시 이름을 제거하고
            cache.append(city_lower)  # 가장 최신으로 삽입
            answer += 1  # 실행시간 1 증가
        else:  # cache miss
            cache.append(city_lower)  # 캐시에 새로운 도시 이름 추가
            answer += 5  # 실행시간 5 증가

    return answer
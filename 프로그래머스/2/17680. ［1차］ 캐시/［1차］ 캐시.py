from collections import deque

def solution(cacheSize, cities):
    answer = 0

    # 캐시 교체 알고리즘(LRU) - 여기 maxlen이 핵심
    cache = deque(maxlen=cacheSize)

    for city in cities:
        # 반드시 소문자로 전부 통일해야!
        city_lower = city.lower()

        # 캐시 히트이면
        if city_lower in cache:
            answer += 1
            cache.remove(city_lower)
            cache.append(city_lower)

        # 캐시 미스이면 
        else:
            cache.append(city_lower)
            answer += 5

    return answer
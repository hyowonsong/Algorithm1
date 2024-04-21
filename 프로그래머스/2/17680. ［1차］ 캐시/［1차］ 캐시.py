# 캐시
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    # 이게 캐시(현재 cache 라고 정의해 둠)
    cache = deque(maxlen = cacheSize)

    for city in cities:
        city_lower = city.lower()
        # 캐시히트이면
        if city_lower in cache:
            answer += 1
            cache.remove(city_lower)
            cache.append(city_lower)

        # 캐시미스이면
        else:
            cache.append(city_lower)
            answer +=5
    return answer
# 캐시(캐시 크기에 따른 실행시간 측정 프로그램)

from collections import deque

def solution(cacheSize, cities):
    answer = 0

    cache = deque(maxlen=cacheSize)

    for city in cities:
        city_lower = city.lower()
        # 캐시히트이면 최신으로 유지해야하기 때문에 remove 필요
        if city_lower in cache:
            answer += 1
            cache.remove(city_lower)
            cache.append(city_lower)
        # 캐시미스이면 가장 오래된 것이 자동으로 삭제되기 때문에 remove 필요없다. 
        else:
            cache.append(city_lower)
            answer += 5
    return answer
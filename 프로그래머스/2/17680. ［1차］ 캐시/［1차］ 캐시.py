def solution(cacheSize, cities):
    answer = 0
    stack = []
    
    for city in cities:
        city = city.lower()  # 대소문자 구분을 없애기 위해 소문자로 변환
        # 캐시에 있는 경우
        if city in stack:
            answer += 1  # 실행 시간 1 증가
            stack.remove(city)  # 해당 도시를 캐시에서 제거
            stack.append(city)  # 캐시의 맨 뒤에 추가하여 최근 사용으로 갱신
        # 캐시에 없는 경우
        else:
            answer += 5  # 실행 시간 5 증가
            # 캐시가 가득 찬 경우
            if len(stack) >= cacheSize and cacheSize > 0:
                stack.pop(0)  # 가장 오래된 도시를 제거
            if cacheSize > 0:  # 캐시 크기가 0보다 큰 경우에만 새로운 도시 추가
                stack.append(city)  # 새로운 도시 추가
    return answer

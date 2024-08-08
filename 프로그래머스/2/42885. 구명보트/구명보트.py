def solution(people, limit):
    answer = 0  
    people.sort()
    
    left = 0 
    right = len(people) - 1  
    
    # while 문을 사용해야
    while left <= right:
        if people[left] + people[right] <= limit:
            # 가장 가벼운 사람과 가장 무거운 사람이 함께 탈 수 있으면
            left += 1  # 가장 가벼운 사람을 태웁니다.
        right -= 1  # 가장 무거운 사람을 태웁니다.
        answer += 1  # 보트 하나를 사용합니다.
    
    return answer
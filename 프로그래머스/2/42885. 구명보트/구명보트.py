def solution(people, limit):
    people.sort()  # 사람들의 몸무게를 오름차순으로 정렬합니다.
    left = 0  # 가장 가벼운 사람을 가리키는 포인터
    right = len(people) - 1  # 가장 무거운 사람을 가리키는 포인터
    answer = 0  # 필요한 구명보트의 수
    
    while left <= right:
        if people[left] + people[right] <= limit:
            # 가장 가벼운 사람과 가장 무거운 사람이 함께 탈 수 있으면
            left += 1  # 가장 가벼운 사람을 태웁니다.
        right -= 1  # 가장 무거운 사람을 태웁니다.
        answer += 1  # 보트 하나를 사용합니다.
    
    return answer
# 구명보트

def solution(people, limit):
    # 몸무게가 가장 많이 나가는 사람과 가장 적게 나가는 사람의 인덱스 초기화
    left, right = 0, len(people) - 1
    # 구명보트 개수 초기화
    answer = 0
    
    # 몸무게가 적은 사람부터 무거운 사람까지 차례로 탐색
    people.sort()
    
    # left와 right가 같아질 때까지 반복
    while left <= right:
        # 가장 적게 나가는 사람과 가장 많이 나가는 사람을 함께 태워 무게를 확인
        if people[left] + people[right] <= limit:
            left += 1  # 가장 적게 나가는 사람을 한 명 태운다
        right -= 1  # 가장 많이 나가는 사람을 항상 태우기 때문에 한 명 태웠다
        
        # 보트 개수를 1 증가시킴
        answer += 1
    
    return answer
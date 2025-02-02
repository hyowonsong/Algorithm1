# 1. 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있다.
# 2.구명보트를 최대한 적게 사용하여 모든 사람 구출
# 3. 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값 return
# left, right로 나누어서 구하는 방법

def solution(people, limit):

    people.sort()
    answer = 0
    
    # 여기서 left 는 0, right는 left가 0부터 시작하니 len(people)-1
    left = 0 
    right = len(people) - 1  

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1  
        
        # 두 명을 태울 수 없는 경우, 가장 무거운 사람은 혼자라도 무조건 보트에 타야 함
        right -= 1
        answer += 1  # 보트를 하나 사용합니다.
    
    return answer
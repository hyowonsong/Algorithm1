def can_cross(stones, k, mid):
    skip = 0  # 연속으로 건너뛰어야 하는 디딤돌의 수
    
    for stone in stones:
        if stone < mid:  # 현재 인원수로 건널 수 없는 돌
            skip += 1
            if skip >= k:  # k개 이상 연속으로 건널 수 없으면 실패
                return False
        else:
            skip = 0  # 건널 수 있는 돌을 만나면 초기화
    
    return True  # 모든 돌을 확인했을 때 건널 수 있으면 True

def solution(stones, k):

    left = 1
    right = 200000000  # 문제의 제한사항에 따른 최대값
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        if can_cross(stones, k, mid):  # mid명이 건널 수 있다면
            answer = mid  # 현재 값을 저장하고
            left = mid + 1  # 더 많은 인원도 가능한지 확인
        else:
            right = mid - 1  # 더 적은 인원으로 시도
            
    return answer
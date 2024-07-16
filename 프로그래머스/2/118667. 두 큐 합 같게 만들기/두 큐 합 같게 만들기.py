# 두 큐 합 같게 만들기

from collections import deque

def solution(queue1, queue2):
    # 두 큐를 합친 전체 합의 절반을 목표로 설정
    target = (sum(queue1) + sum(queue2)) // 2
    
    # 각 큐의 현재 합 계산
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    # 두 큐를 deque로 변환
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    # 전체 길이의 3배를 최대 반복 횟수로 설정
    max_iterations = len(queue1) * 3
    count = 0
    
    while count < max_iterations:
        if sum1 == target:
            return count
        elif sum1 > target:
            value = q1.popleft()
            q2.append(value)
            sum1 -= value
            sum2 += value
        else:
            value = q2.popleft()
            q1.append(value)
            sum1 += value
            sum2 -= value
        count += 1
    
    # 목표를 달성할 수 없는 경우
    return -1

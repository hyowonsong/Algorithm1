from collections import deque

def solution(queue1, queue2):
    # 두 큐를 데크로 변환
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    # 두 큐의 합 계산
    sum1, sum2 = sum(queue1), sum(queue2)
    total_sum = sum1 + sum2
    
    # 목표 합 계산
    if total_sum % 2 != 0:
        return -1
    target = total_sum // 2
    
    # 투 포인터 초기화
    total = queue1 + queue2  # 두 큐를 이어붙인 배열
    n = len(total)
    left, right = 0, len(queue1)
    current_sum = sum1
    max_moves = n * 2  # 최대 이동 횟수 제한
    
    for moves in range(max_moves):
        if current_sum == target:
            return moves
        if current_sum < target:  # 목표 합보다 작으면 오른쪽에서 추가
            current_sum += total[right]
            right = (right + 1) % n
        else:  # 목표 합보다 크면 왼쪽에서 제거
            current_sum -= total[left]
            left = (left + 1) % n
            
    return -1

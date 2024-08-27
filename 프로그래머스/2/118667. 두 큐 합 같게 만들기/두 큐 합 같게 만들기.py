from collections import deque

def solution(queue1, queue2):
    # 두 큐의 합을 계산
    total1, total2 = sum(queue1), sum(queue2)
    total = total1 + total2
    
    # 만약 전체 합이 홀수라면, 두 큐를 같은 합으로 만들 수 없음
    if total % 2 != 0:
        return -1
    
    # 목표 합
    target = total // 2
    
    # 두 큐를 deque로 변환 후 양쪽에서 pop,append 효율적으로 수행할 수 있게 함
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    # 포인터 초기화
    count = 0
    max_iterations = len(q1) * 3
    
    while total1 != target:
        if total1 > target:
            # q1에서 원소를 빼서 q2로 이동
            num = q1.popleft()
            total1 -= num
            q2.append(num)
        else:
            # q2에서 원소를 빼서 q1으로 이동
            num = q2.popleft()
            total1 += num
            q1.append(num)
        
        count += 1
        
        # 이동 횟수가 최대 횟수를 초과하면 더 이상 가능하지 않음
        if count > max_iterations:
            return -1
    
    return count

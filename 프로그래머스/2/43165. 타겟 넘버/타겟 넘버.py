from collections import deque  

def solution(numbers, target):
    answer = 0  
    queue = deque() 
    queue.append((0, 0))  # 큐에 초기값 (인덱스 0, 계산값 0)을 추가합니다.

    while queue:  # 큐가 비어있지 않은 동안 반복합니다.
        i, value = queue.popleft() 

        if i == len(numbers) and value == target:  # 인덱스가 리스트의 길이와 같고, 계산값이 타겟과 같다면
            answer += 1  #                    결과값을 1 증가시킵니다.
        elif i == len(numbers):              # 인덱스가 리스트의 길이와 같다면 다시 while문
            pass                                    
        else:                                          # 그 외의 경우
            queue.append((i + 1, value + numbers[i]))  # 현재 숫자를 더한 새로운 튜플을 큐에 추가합니다.
            queue.append((i + 1, value - numbers[i]))  # 현재 숫자를 뺀 새로운 튜플을 큐에 추가합니다.

    return answer  
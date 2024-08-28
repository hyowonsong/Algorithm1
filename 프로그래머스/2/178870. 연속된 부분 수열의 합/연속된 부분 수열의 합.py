def solution(sequence, k):
    start = 0
    current_sum = 0
    min_length = float('inf')  # 초기화: 매우 큰 값
    result = [-1, -1]  # 결과를 저장할 변수
    
    # `end` 포인터를 이동시키며 윈도우 확장
    for end in range(len(sequence)):
        current_sum += sequence[end]
        
        # `current_sum`이 `k`보다 클 때까지 `start` 포인터 이동
        while current_sum > k and start <= end:
            current_sum -= sequence[start]
            start += 1
        
        # `current_sum`이 `k`와 같을 때, 부분 수열의 길이 계산 및 업데이트
        if current_sum == k:
            if (end - start) < min_length:
                min_length = end - start
                result = [start, end]
    
    return result
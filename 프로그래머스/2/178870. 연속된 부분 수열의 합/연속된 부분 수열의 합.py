def solution(sequence, k):
    # 수열의 길이
    n = len(sequence)
    
    # 투 포인터 초기화
    start = 0
    end = 0
    
    # 현재 부분 수열의 합 초기화
    current_sum = sequence[0]
    
    # 가장 짧은 부분 수열의 길이와 인덱스 초기화
    min_length = float('inf')
    result = [0, 0]

    # 수열을 순회하면서 부분 수열 찾기
    while end < n:
        if current_sum < k:
            # 현재 합이 k보다 작으면 end 포인터를 오른쪽으로 이동
            end += 1
            if end < n:
                current_sum += sequence[end]
        elif current_sum >= k:
            if current_sum == k:
                # 합이 k와 같고, 현재 부분 수열이 이전에 찾은 것보다 짧으면 업데이트
                length = end - start + 1
                if length < min_length:
                    min_length = length
                    result = [start, end]
            
            # start 포인터를 오른쪽으로 이동
            current_sum -= sequence[start]
            start += 1

    # 찾은 부분 수열의 시작과 끝 인덱스 반환
    return result
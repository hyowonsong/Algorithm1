# 연속된 부분 수열의 합

def solution(sequence, k):
    n = len(sequence)
    left, right = 0, 0  # 투 포인터의 시작점
    current_sum = 0  # 현재 부분 수열의 합
    result = [0, n-1]  # 결과를 저장할 리스트, 초기값은 전체 수열

    while right < n:
        # 오른쪽 포인터를 이동하며 합을 증가
        current_sum += sequence[right]
        
        # 현재 합이 k보다 크면 왼쪽 포인터를 이동하며 합을 감소
        while current_sum > k and left <= right:
            current_sum -= sequence[left]
            left += 1
        
        # 현재 합이 k와 같으면 결과 업데이트 검토
        if current_sum == k:
            # 현재 부분 수열의 길이가 저장된 결과보다 짧으면 업데이트
            if right - left < result[1] - result[0]:
                result = [left, right]
        
        right += 1  # 다음 요소로 이동

    return result  # 최종 결과 반환
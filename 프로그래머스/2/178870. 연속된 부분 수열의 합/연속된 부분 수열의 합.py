# 연속된 부분 수열의 합

def solution(sequence, k):
    left = 0
    right = 0
    current_sum = sequence[0]

    n = len(sequence)
    min_length = float('inf')
    answer = [0,0]

    # 투포인터 시작 (while문)
    while right < n:
        # current_sum이 k인 경우의 조건들을 먼저 전부 나열
        if current_sum == k:
            # 현재의 길이를 찾습니다.
            current_length = right-left + 1

            # 현재의 길이와 min_length를 비교해서 만약 현재의 길이가 더 짧다면 min_length 교체
            if current_length < min_length:
                min_length = current_length
                answer = [left, right]
            # 길이가 짧은 수열이 여러 개인 경우 현재의 맨 왼쪽이 이전 결과의 맨 왼쪽보다 더 작으면 교체 
            elif current_length == min_length and left<answer[0]:
                answer = [left, right]

            # left를 이동해 다음 구간 확인(계속 확인해줘야 한다.)
            current_sum -= sequence[left]
            left += 1

        # current_sum이 k보다 작은 경우
        elif current_sum < k:
            right += 1
            if right < n:
                current_sum += sequence[right]

        # current_sum이 k보다 큰 경우 left를 증가시켜 구간 축소
        else:
            current_sum -= sequence[left]
            left += 1
    
    return answer
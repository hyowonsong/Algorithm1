# 연속된 부분 수열의 합

# 1. 두 인덱스의 원소와 그 사이의 원소를 모두 포함
# 2. 부분 수열의 합은 K
# 3. 합이 k인 부분 수열이 여러 개 -> 길이 가장 짧은 수열 찾기
# 4. 길이가 짧은 수열이 여러 개 -> 앞쪽에 나오는 수열을 찾기

def solution(sequence, k):
    # 1. 초기화
    left = 0
    right = 0
    current_sum = sequence[0] # 현재 구간의 합을 추적

    n = len(sequence)
    min_length = float('inf')
    result = [0, 0]

    # 2. while 루프프
    while right < n:
        # 2-1.현재 구간이 조건을 만족하므로 길이를 확인하고 결과를 갱신신
        if current_sum == k:
            current_length = right - left + 1

            if current_length < min_length:
                min_length = current_length
                result = [left, right]

            elif current_length == min_length and left < result[0]:
                # 길이가 같다면 더 앞쪽에 나온 구간 선택
                result = [left, right]

            # left를 이동해 다음 구간 확인
            current_sum -= sequence[left]
            left += 1

        # 2-2. 작기 때문에 right를 증가시켜 구간을 확장
        elif current_sum < k:
            right += 1
            if right < n:
                current_sum += sequence[right]
        # 2-3. 더 큰 경우이기 때문에 left를 증가시켜 구간을 축소소
        else:
            current_sum -= sequence[left]
            left += 1

    return result
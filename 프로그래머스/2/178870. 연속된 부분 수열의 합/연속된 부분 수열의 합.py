# 연속된 부분 수열의 합
# 기본적으로 오른쪽 포인터를 이동시키며 부분 수열의 합을 증가시키고, 
# 그 합이 목표값 k보다 크면 왼쪽 포인터를 이동시켜 부분 수열의 합을 줄이는 식으로 작동

def solution(sequence, k):
    n = len(sequence)  # 수열의 길이
    left, right = 0, 0  # 두 개의 포인터 초기화 (부분 수열의 시작과 끝 인덱스)
    current_sum = sequence[0]  # 현재 부분 수열의 합을 첫 번째 원소로 초기화
    min_length = float('inf')  # 최소 길이를 무한대로 초기화 (최소 길이를 찾기 위해)
    result = []  # 결과를 저장할 리스트 초기화

    while right < n:  # 오른쪽 포인터가 수열의 끝에 도달할 때까지 반복
        if current_sum < k:
            # 현재 부분 수열의 합이 k보다 작으면 오른쪽 포인터를 오른쪽으로 이동
            right += 1
            if right < n:
                current_sum += sequence[right]  # 오른쪽 포인터가 가리키는 값을 현재 합에 더함
        elif current_sum > k:
            # 현재 부분 수열의 합이 k보다 크면 왼쪽 포인터를 오른쪽으로 이동
            current_sum -= sequence[left]  # 왼쪽 포인터가 가리키는 값을 현재 합에서 뺌
            left += 1
        else:  # current_sum == k
            # 현재 부분 수열의 합이 k와 같을 때
            if (right - left + 1) < min_length:
                # 부분 수열의 길이가 최소 길이보다 짧으면
                min_length = right - left + 1  # 최소 길이를 갱신
                result = [left, right]  # 결과를 현재 부분 수열의 시작과 끝 인덱스로 갱신
            current_sum -= sequence[left]  # 왼쪽 포인터가 가리키는 값을 현재 합에서 뺌
            left += 1

    return result  # 조건을 만족하는 부분 수열의 시작과 끝 인덱스를 반환
# 부분 수열의 합

# 부분 수열의 합을 계산하는 재귀 함수
def solution(arr, K, index=0, current_sum=0):
    if index == len(arr):
        # 현재의 합이 K와 같으면 1을 반환, 아니면 0을 반환
        if current_sum == K:
            return 1
        else:
            return 0
    
    # 현재 원소를 포함하지 않는 경우의 합을 계산
    count_without_current = solution(arr, K, index + 1, current_sum)
    
    # 현재 원소를 포함하는 경우의 합을 계산
    count_with_current = solution(arr, K, index + 1, current_sum + arr[index])
    
    # 두 경우의 합을 반환
    return count_without_current + count_with_current


T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    # 합이 0인 경우(아무것도 선택하지 않는 경우)는 제외해야 하므로
    # K가 0일 때는 1을 빼고, 그렇지 않으면 0을 뺀다
    if K == 0:
        result = solution(A, K) - 1  # K가 0이면 1 빼기
    else:
        result = solution(A, K)  # K가 0이 아닐 경우 그대로 결과

    print(f"#{t} {result}")

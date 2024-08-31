# 수들의 합

S = int(input())

def solution(S):
    # 이분 탐색을 위한 초기값 설정
    left, right = 1, 4294967295  # 넉넉한 범위로 설정

    while left <= right:
        mid = (left + right) // 2
        # 연속된 자연수의 합 계산
        current_sum = mid * (mid + 1) // 2
        
        if current_sum <= S:
            left = mid + 1  # 더 큰 N을 찾기 위해
        else:
            right = mid - 1  # 더 작은 N으로 조정

    return right

# 결과 출력
print(solution(S))

def solution(n, times):
    left = 1
    right = max(times) * n
    # 최소 시간을 저장할 변수 (초기값은 최대 시간으로 설정)
    answer = right

    # 이분 탐색을 수행
    while left <= right:
        # 중간값 계산 (현재 시간의 후보)
        mid = (left + right) // 2
        
        # 현재 시간(mid) 동안 각 심사관이 처리할 수 있는 사람의 수를 계산
        total_people = 0  # 처리 가능한 총 사람 수 초기화
        for time in times:
            total_people += mid // time  # 각 심사관이 mid 시간 동안 처리할 수 있는 사람 수를 더함

        # 만약 현재 시간 동안 처리 가능한 사람이 n명 이상이라면
        if total_people >= n:
            # 최소 시간을 갱신 (현재 mid가 가능한 최소 시간일 수 있음)
            answer = mid
            # 시간을 더 줄이기 위해 오른쪽 끝을 줄임
            right = mid - 1
        else:
            # 처리 가능한 사람이 부족하면 시간을 늘리기 위해 왼쪽 끝을 늘림
            left = mid + 1

    # 탐색이 종료되면 최소 시간이 answer에 저장됨
    return answer

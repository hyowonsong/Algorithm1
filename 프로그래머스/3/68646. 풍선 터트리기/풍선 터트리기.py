def solution(a):
    # 길이가 1 이하일 경우, 모든 풍선을 남길 수 있음
    if len(a) <= 1:
        return len(a)
    
    # 왼쪽 최소값 배열 생성
    left_min = [0] * len(a)
    left_min[0] = a[0]
    for i in range(1, len(a)):
        left_min[i] = min(left_min[i - 1], a[i])
    
    # 오른쪽 최소값 배열 생성
    right_min = [0] * len(a)
    right_min[-1] = a[-1]
    for i in range(len(a) - 2, -1, -1):
        right_min[i] = min(right_min[i + 1], a[i])
    
    # 조건을 만족하는 풍선 개수 계산
    count = 0
    for i in range(len(a)):
        # 현재 풍선이 왼쪽 최소값 또는 오른쪽 최소값보다 작다면 남길 수 있음
        if a[i] <= left_min[i] or a[i] <= right_min[i]:
            count += 1
    
    return count

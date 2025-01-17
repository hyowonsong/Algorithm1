def solution(diffs, times, limit):
    def time_needed(level):
        total_time = 0
        prev_time = 0  # 이전 퍼즐의 소요 시간
        
        for diff, time_cur in zip(diffs, times):
            if diff <= level:
                total_time += time_cur
            else:
                mistakes = diff - level
                total_time += mistakes * (time_cur + prev_time) + time_cur
            
            prev_time = time_cur  # 현재 퍼즐의 시간을 이전 퍼즐 시간으로 업데이트
            
            if total_time > limit:
                return total_time  # 제한 시간 초과 시 조기 종료
        
        return total_time

    # 이분 탐색 범위 설정
    left, right = 1, max(diffs)
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        if time_needed(mid) <= limit:
            answer = mid
            right = mid - 1  # 더 낮은 숙련도를 탐색
        else:
            left = mid + 1  # 더 높은 숙련도를 탐색
    
    return answer
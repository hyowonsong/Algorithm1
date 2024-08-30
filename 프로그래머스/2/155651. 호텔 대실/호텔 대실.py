import heapq

def time_to_minutes(t):
    hours, minutes = map(int, t.split(':'))
    # 시간을 분 단위로 변환
    return hours * 60 + minutes  

def solution(book_time):
    # 변환된 예약 시간 리스트
    reservations = []
    
    for start, end in book_time:
        start_min = time_to_minutes(start)  # 시작 시간을 분으로 변환
        end_min = time_to_minutes(end)  # 종료 시간을 분으로 변환
        reservations.append((start_min, end_min + 10))  # 종료 시간에 청소 시간 10분 추가
    
    # 시작 시간을 기준으로 예약 정렬
    reservations.sort(key=lambda x: x[0])
    
    # 우선순위 큐로 객실 사용 상태 추적
    room_end_times = []
    
    for start, end in reservations:
        if room_end_times and room_end_times[0] <= start:
            # 사용 가능한 객실이 있으면 해당 객실 제거
            heapq.heappop(room_end_times)
        # 현재 예약의 종료 시간을 힙에 추가 (새 객실 할당 또는 기존 객실 재사용)
        heapq.heappush(room_end_times, end)
    
    return len(room_end_times)  # 필요한 총 객실 수 반환
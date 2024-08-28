import heapq

def time_to_minutes(t):
    hours, minutes = map(int, t.split(':'))
    return hours * 60 + minutes

def solution(book_time):
    # 변환된 예약 시간 리스트
    reservations = []
    
    for start, end in book_time:
        start_min = time_to_minutes(start)
        end_min = time_to_minutes(end)
        # 종료 시간 + 10분 청소 시간
        reservations.append((start_min, end_min + 10))  
    
    # 시작 시간을 기준으로 정렬
    reservations.sort(key=lambda x: x[0])
    
    # 우선순위 큐를 사용하여 현재 객실 사용 상태를 추적
    room_end_times = []
    
    for start, end in reservations:
        if room_end_times and room_end_times[0] <= start:
            heapq.heapreplace(room_end_times, end)
        else:
            heapq.heappush(room_end_times, end)
    
    return len(room_end_times)
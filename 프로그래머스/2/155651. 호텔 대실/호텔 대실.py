import heapq

def solution(book_time):
    def time_to_minute(time_str):
        h, m = map(int, time_str.split(':'))
        return h * 60 + m
    
    # 예약 시간을 분 단위로 변환
    timeline = []
    for start, end in book_time:
        start_minute = time_to_minute(start)
        end_minute = time_to_minute(end)
        timeline.append((start_minute, end_minute))
    
    # 시작 시간을 기준으로 정렬
    timeline.sort()
    
    room_end_times = []
    max_rooms = 0
    
    for start, end in timeline:
        # 청소 시간 10분 추가
        end += 10
        
        # 현재 시작 시간 이전에 끝나는 방들 제거
        while room_end_times and room_end_times[0] <= start:
            heapq.heappop(room_end_times)
        
        # 새로운 방 추가
        heapq.heappush(room_end_times, end)
        
        # 최대 방 개수 업데이트
        max_rooms = max(max_rooms, len(room_end_times))
    
    return max_rooms
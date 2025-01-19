def solution(plans):
    # 시간 변환 함수
    def time_to_minutes(time_str):
        h, m = map(int, time_str.split(":"))
        return h * 60 + m
    
    # plans 정렬: 시작 시간을 기준으로 오름차순
    plans.sort(key=lambda x: time_to_minutes(x[1]))
    
    # 멈춰둔 과제를 저장할 스택
    paused_tasks = []
    # 결과 저장
    completed_tasks = []
    # 현재 시각
    current_time = 0
    
    for i, (name, start, playtime) in enumerate(plans):
        start_time = time_to_minutes(start)
        playtime = int(playtime)
        
        # 이전 과제를 처리
        while paused_tasks and current_time < start_time:
            paused_name, remaining_time = paused_tasks.pop()
            if current_time + remaining_time <= start_time:
                # 과제를 끝낼 수 있음
                current_time += remaining_time
                completed_tasks.append(paused_name)
            else:
                # 아직 과제를 끝내지 못했으므로 남은 시간을 저장
                paused_tasks.append((paused_name, remaining_time - (start_time - current_time)))
                current_time = start_time
                break
        
        # 현재 과제를 시작
        current_time = max(current_time, start_time)
        if i + 1 < len(plans):
            next_start_time = time_to_minutes(plans[i + 1][1])
            if current_time + playtime <= next_start_time:
                # 현재 과제를 끝낼 수 있음
                current_time += playtime
                completed_tasks.append(name)
            else:
                # 과제를 끝내지 못했으므로 남은 시간을 저장
                paused_tasks.append((name, current_time + playtime - next_start_time))
                current_time = next_start_time
        else:
            # 마지막 과제는 끝까지 처리
            completed_tasks.append(name)
            current_time += playtime
    
    # 남아 있는 멈춘 과제를 처리
    while paused_tasks:
        completed_tasks.append(paused_tasks.pop()[0])
    
    return completed_tasks
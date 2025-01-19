def solution(plans):
    # 시간 변환 함수: "HH:MM" 형식의 시간을 분 단위로 변환
    def time_to_minutes(time_str):
        h, m = map(int, time_str.split(":"))  # 시간과 분을 분리하여 정수로 변환
        return h * 60 + m  # 시간을 분 단위로 변환 후 분과 더함

    # plans 정렬: 시작 시간을 기준으로 오름차순 정렬
    plans.sort(key=lambda x: time_to_minutes(x[1]))

    # 멈춰둔 과제를 저장할 스택
    paused_tasks = []
    # 완료된 과제의 이름을 저장할 리스트
    completed_tasks = []
    # 현재 시각을 기록하는 변수
    current_time = 0

    # 각 과제 정보를 순회
    for i, (name, start, playtime) in enumerate(plans):
        start_time = time_to_minutes(start)  # 과제의 시작 시간을 분 단위로 변환
        playtime = int(playtime)  # 실행 시간을 정수로 변환

        # 멈춰둔 과제를 처리
        while paused_tasks and current_time < start_time:
            paused_name, remaining_time = paused_tasks.pop()  # 가장 최근에 멈춘 과제를 가져옴
            if current_time + remaining_time <= start_time:
                # 현재 시간 내에 과제를 끝낼 수 있는 경우
                current_time += remaining_time  # 과제를 끝내고 현재 시각 갱신
                completed_tasks.append(paused_name)  # 과제를 완료 리스트에 추가
            else:
                # 현재 시간 내에 과제를 끝낼 수 없는 경우
                paused_tasks.append((paused_name, remaining_time - (start_time - current_time)))
                # 과제의 남은 시간을 다시 스택에 저장
                current_time = start_time  # 현재 시각을 과제 시작 시간으로 설정
                break  # 반복문 종료

        # 현재 과제를 시작
        current_time = max(current_time, start_time)  # 현재 시각이 시작 시간보다 작으면 시작 시간으로 갱신
        if i + 1 < len(plans):  # 다음 과제가 존재하는 경우
            next_start_time = time_to_minutes(plans[i + 1][1])  # 다음 과제 시작 시간을 계산
            if current_time + playtime <= next_start_time:
                # 현재 과제를 끝낼 수 있는 경우
                current_time += playtime  # 과제를 끝내고 현재 시각 갱신
                completed_tasks.append(name)  # 과제를 완료 리스트에 추가
            else:
                # 현재 과제를 끝낼 수 없는 경우
                paused_tasks.append((name, current_time + playtime - next_start_time))
                # 과제의 남은 시간을 스택에 저장
                current_time = next_start_time  # 현재 시각을 다음 과제 시작 시간으로 설정
        else:
            # 마지막 과제인 경우
            completed_tasks.append(name)  # 과제를 완료 리스트에 추가
            current_time += playtime  # 과제를 끝내고 현재 시각 갱신

    # 남아 있는 멈춰둔 과제를 처리
    while paused_tasks:
        completed_tasks.append(paused_tasks.pop()[0])  # 스택에서 과제를 꺼내 완료 리스트에 추가

    return completed_tasks  # 완료된 과제 리스트를 반환
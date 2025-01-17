def solution(id_list, report, k):
    # 유저별로 신고당한 횟수를 저장할 딕셔너리 초기화
    report_count = {}
    for user in id_list:
        report_count[user] = 0  # 각 유저의 신고당한 횟수를 0으로 초기화

    # 유저별로 신고한 ID를 저장할 딕셔너리 초기화
    user_reports = {}
    for user in id_list:
        user_reports[user] = set()  # 중복 신고를 방지하기 위해 집합으로 초기화
    
    # 신고 기록 처리
    for entry in report:
        reporter, reported = entry.split()  # 신고자와 신고당한 유저를 분리
        if reported not in user_reports[reporter]:  # 신고자가 해당 유저를 처음 신고하는 경우
            user_reports[reporter].add(reported)  # 신고자의 신고 리스트에 추가
    
    # 신고당한 횟수 계산
    for reporter in user_reports:  # 모든 유저의 신고 기록을 순회
        for reported in user_reports[reporter]:  # 신고자가 신고한 유저들을 확인
            report_count[reported] += 1  # 신고당한 유저의 신고 횟수를 1 증가
    
    # 정지된 유저 리스트 생성
    banned_users = set()  # 정지된 유저를 저장할 집합 초기화
    for user, count in report_count.items():  # 각 유저의 신고당한 횟수를 확인
        if count >= k:  # 신고당한 횟수가 기준값 k 이상인 경우
            banned_users.add(user)  # 해당 유저를 정지 리스트에 추가
    
    # 결과 메일 발송 횟수 계산
    result = []  
    for user in id_list:  # 모든 유저를 순회하며
        mail_count = 0  # 해당 유저가 받을 결과 메일 수를 초기화
        for reported in user_reports[user]:  # 해당 유저가 신고한 유저들을 확인
            if reported in banned_users:  # 신고한 유저가 정지된 유저 리스트에 포함된 경우
                mail_count += 1  # 결과 메일 수를 1 증가
        result.append(mail_count)  # 최종 결과 메일 수를 결과 리스트에 추가
    
    return result

def solution(survey, choices):
    # 각 지표별 점수를 저장할 딕셔너리
    # 각 성격 유형의 초기 점수를 0으로 설정
    scores = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    # 선택에 따른 점수
    # 인덱스 + 1이 선택지 번호, 값이 해당 점수
    choice_scores = [3, 2, 1, 0, 1, 2, 3]
    
    # 각 질문에 대한 점수 계산
    for i in range(len(survey)):
        # 선택이 4(모르겠음) 미만인 경우, 첫 번째 성격 유형에 점수 부여
        if choices[i] < 4:
            scores[survey[i][0]] += choice_scores[choices[i]-1]
        # 선택이 4(모르겠음) 초과인 경우, 두 번째 성격 유형에 점수 부여
        elif choices[i] > 4:
            scores[survey[i][1]] += choice_scores[choices[i]-1]
        # 선택이 4(모르겠음)인 경우, 아무 점수도 부여하지 않음
    
    # 최종 성격 유형 결정
    result = ''
    # 각 지표별 성격 유형 쌍
    indicators = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    
    # 각 지표별로 점수 비교
    for a, b in indicators:
        # 첫 번째 성격 유형의 점수가 크거나 같으면 첫 번째 선택
        # (같은 경우 사전순으로 앞서는 것을 선택)
        if scores[a] >= scores[b]:
            result += a
        # 두 번째 성격 유형의 점수가 더 크면 두 번째 선택
        else:
            result += b
    
    # 최종적으로 결정된 성격 유형 반환
    return result
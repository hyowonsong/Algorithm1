def solution(survey, choices):
    # 성격 유형 별 점수를 저장할 딕셔너리
    scores = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 
              'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    # 선택지 점수 매핑
    choice_scores = {
        1: 3,  # 매우 비동의
        2: 2,  # 비동의
        3: 1,  # 약간 비동의
        4: 0,  # 모르겠음
        5: 1,  # 약간 동의
        6: 2,  # 동의
        7: 3   # 매우 동의
    }
    
    for i in range(len(survey)):
        s = survey[i]
        c = choices[i]
        
        # 선택지에 따른 점수
        score = choice_scores[c]
        
        if c < 4:  # 비동의 관련 성격
            scores[s[0]] += score
        elif c > 4:  # 동의 관련 성격
            scores[s[1]] += score

    # 성격 유형을 결정하기 위한 결과 문자열
    result = ""
    for pair in [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]:
        a, b = pair
        if scores[a] > scores[b]:
            result += a
        elif scores[a] < scores[b]:
            result += b
        else:
            result += min(a, b)
    
    return result
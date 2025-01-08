# 성격 유형 검사하기

def solution(survey, choices):
    # 초기화: 성격 유형 점수 저장용 딕셔너리
    scores = {
        'R': 0, 'T': 0,
        'C': 0, 'F': 0,
        'J': 0, 'M': 0,
        'A': 0, 'N': 0
    }
    
    # 점수 계산
    for i in range(len(survey)):
        agree, disagree = survey[i][1], survey[i][0]
        choice = choices[i]
        
        if choice < 4:  # 비동의
            scores[disagree] += 4 - choice
        elif choice > 4:  # 동의
            scores[agree] += choice - 4

    # 성격 유형 결정
    # (현재 1,2,3,4번 지표가 순서대로 있어 아래와 같이 하면 자연스럽게 순서대로 들어간다.)
    result = []
    if scores['R'] >= scores['T']:
        result.append('R')
    else:
        result.append('T')

    if scores['C'] >= scores['F']:
        result.append('C')
    else:
        result.append('F')

    if scores['J'] >= scores['M']:
        result.append('J')
    else:
        result.append('M')

    if scores['A'] >= scores['N']:
        result.append('A')
    else:
        result.append('N')
    
    # 결과 반환
    return ''.join(result)

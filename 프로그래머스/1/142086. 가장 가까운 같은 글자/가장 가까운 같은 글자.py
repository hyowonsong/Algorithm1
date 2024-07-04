def solution(s):
    last_seen = {}  # 각 문자의 마지막 출현 위치를 기록할 딕셔너리
    result = []  # 결과 리스트
    
    for i, char in enumerate(s):
        if char in last_seen:
            result.append(i - last_seen[char])
        else:
            result.append(-1)
        
        # 현재 문자의 마지막 출현 위치 갱신
        last_seen[char] = i
    
    return result
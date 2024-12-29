def solution(s):
    last_seen = {}  # 딕셔너리
    answer = []     

    for i, char in enumerate(s):
        if char in last_seen:
            # 해당 문자가 이전에 등장했다면 현재 인덱스와의 차이를 계산
            answer.append(i - last_seen[char])
        else:
            # 이전에 등장하지 않았다면 -1 추가
            answer.append(-1)

        # 현재 문자의 위치를 갱신
        last_seen[char] = i

    return answer
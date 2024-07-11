def solution(s, skip, index):
    # 모든 알파벳을 문자열로 정의
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # skip 리스트에 있는 알파벳을 제외한 문자열 생성
    skip = set(skip)
    available = []
    
    # 모든 알파벳을 순회하면서 skip에 없는 알파벳만 available에 추가
    for ch in alphabet:
        if ch not in skip:
            available.append(ch)

    # 변환된 결과를 저장할 리스트
    result = []

    for char in s:
        # 현재 문자의 위치를 찾음
        current = available.index(char)
        # index만큼 이동한 위치를 계산
        new_pos = (current + index) % len(available)
        # 변환된 문자를 결과 리스트에 추가
        result.append(available[new_pos])

    # 결과 리스트를 문자열로 변환하여 반환
    return ''.join(result)
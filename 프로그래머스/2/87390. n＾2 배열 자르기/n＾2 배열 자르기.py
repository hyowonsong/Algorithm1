def solution(n, left, right):

    # left에서 right 사이의 구간을 추출
    result = []
    for idx in range(left, right + 1):
        # idx 위치의 값 계산
        # idx를 0부터 시작하는 인덱스로 변환
        row = idx // n
        col = idx % n
        value = max(row, col) + 1
        result.append(value)
    
    return result
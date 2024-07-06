
def solution(n, left, right):

    # left에서 right 사이의 구간을 추출
    result = []
    for idx in range(left, right + 1):
        # idx 위치의 값 계산
        # idx를 0부터 시작하는 인덱스로 변환

        # 인덱스 2에서 5까지를 순회하면서 각 위치의 값을 계산합니다.
        # 인덱스를 2차원 배열의 행과 열로 변환하여 값을 결정합니다.
        # 예를 들어, 인덱스 2를 변환하면:
        # row = 2 // 3 = 0 (행)
        # col = 2 % 3 = 2 (열)
        # 따라서 2차원 배열에서의 위치는 (0, 2)가 되고, 값은 max(0, 2) + 1 = 3이 됩니다.

        row = idx // n
        col = idx % n
        value = max(row, col) + 1
        result.append(value)
    
    return result

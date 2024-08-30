def find_one_positions(n):
    positions = []
    position = 0
    while n > 0:
        if n & 1:  # 최하위 비트가 1인지 확인
            positions.append(str(position))
        n >>= 1  # 오른쪽으로 1비트 시프트
        position += 1
    return ' '.join(positions)

T = int(input())  # 테스트 케이스 개수
for i in range(T):
    n = int(input())
    print(find_one_positions(n))
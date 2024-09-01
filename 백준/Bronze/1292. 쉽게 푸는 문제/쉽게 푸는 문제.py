A, B = map(int, input().split())

def find_sum(A, B):
    # 수열 생성 및 합 계산을 위한 변수
    sequence = []
    current_number = 1
    
    # 수열이 A번째까지의 숫자들을 생성합니다.
    while len(sequence) < B:
        sequence.extend([current_number] * current_number)
        current_number += 1
    
    # 구간의 합을 계산합니다.
    # 인덱스는 0부터 시작하므로 A-1, B-1로 조정
    return sum(sequence[A-1:B])

print(find_sum(A, B))

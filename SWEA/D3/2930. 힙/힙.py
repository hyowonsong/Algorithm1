# 힙

import heapq  # heapq 모듈은 최소 힙을 제공

# 테스트 케이스 수 입력
T = int(input())

# 각 테스트 케이스에 대해 처리
for t in range(1, T + 1):
    # 연산의 개수 입력
    N = int(input())
    
    # 최대 힙을 구현할 리스트
    max_heap = []
    
    # 출력 결과 저장할 리스트
    results = []
    
    # N개의 연산에 대해 처리
    for _ in range(N):
        operation = input().split()
        
        # 연산 1: 자연수 x 삽입
        if operation[0] == '1':
            x = int(operation[1])
            # 음수로 변환하여 삽입 -> 최대 힙 구현
            heapq.heappush(max_heap, -x)
        
        # 연산 2: 최대값 출력 후 제거
        elif operation[0] == '2':
            if max_heap:
                # 최대값 출력 (음수로 변환되어 있으니 다시 양수로 돌림)
                results.append(-heapq.heappop(max_heap))
            else:
                # 힙이 비어있으면 -1 출력
                results.append(-1)
    
    # 출력 형식 맞추기
    print(f"#{t} {' '.join(map(str, results))}")

T = int(input())  

for t in range(1, T + 1):
    # 두 숫자열의 크기 N, M 입력
    N, M = map(int, input().split())
    
    # 숫자열 Ai와 Bj 입력
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    # Ai가 더 길면 두 리스트를 바꿔줌 (Ai가 항상 짧은 리스트가 되도록)
    if N > M:
        Ai, Bj = Bj, Ai
        N, M = M, N

    # 가능한 최대 곱셈 합을 저장할 변수 (이거 까먹으면 안됨)
    max_sum = float('-inf')  

    # Ai를 Bj의 각 위치에 맞추어 이동시켜가면서 최대 곱셈 합 계산
    for i in range(M - N + 1):
        
        current_sum = 0
        for j in range(N):
            current_sum += Ai[j] * Bj[i + j]
        # 최대값 갱신
        max_sum = max(max_sum, current_sum)

    # 결과 출력
    print(f'#{t} {max_sum}')
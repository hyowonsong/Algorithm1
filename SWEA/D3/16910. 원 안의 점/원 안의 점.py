T = int(input())  

for t in range(1, T + 1):
    N = int(input())  
    # 격자점의 개수를 세기 위한 변수
    count = 0  

    # (x, y) 좌표를 순차적으로 확인
    for x in range(-N, N + 1):
        for y in range(-N, N + 1):
            if x * x + y * y <= N * N:  # x^2 + y^2 <= N^2인 경우
                count += 1  # 조건을 만족하면 count 증가

    # 결과 출력
    print(f'#{t} {count}')
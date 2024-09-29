# 파스칼의 삼각형

T = int(input())  

for t in range(1, T+1):
    N = int(input()) 
    triangle = []  

    # 파스칼 삼각형 만들기
    for i in range(N):
        # 각 줄의 첫 번째와 마지막 숫자는 1 이기 때문에 전부 1로 정의
        row = [1] * (i+1)

        # 중간 숫자들 계산 (3번째 줄부터)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        # 완성된 줄을 삼각형에 추가
        triangle.append(row)


    # 숫자들을 한 칸씩 띄워서 출력
    print(f'#{t}')
    for row in triangle:
        print(' '.join(map(str, row)))

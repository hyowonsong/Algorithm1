T = 10  
for i in range(1, T + 1):
    # 덤프 횟수
    n = int(input())
    dumps = list(map(int, input().split()))

    # 주어진 덤프 횟수만큼 작업 수행
    for _ in range(n):
        # 최고점에서 1을 빼고, 최저점에 1을 더한다
        max_index = dumps.index(max(dumps))
        min_index = dumps.index(min(dumps))
        
        dumps[max_index] -= 1
        dumps[min_index] += 1

        # 최고점과 최저점 차이가 1이하가 되면 평탄화 완료
        if max(dumps) - min(dumps) <= 1:
            break

    # 결과 출력
    print(f'#{i} {max(dumps) - min(dumps)}')
# 입력: 국가 수 N과 순위를 알고 싶은 국가 K
N, K = map(int, input().split())

# 국가와 메달 정보를 저장할 리스트
medals = []

# 각 국가의 메달 정보 입력 받기
for _ in range(N):
    country, gold, silver, bronze = map(int, input().split())
    medals.append((country, gold, silver, bronze))

# 메달 리스트를 금, 은, 동메달 순으로 내림차순 정렬
medals.sort(key=lambda x: (-x[1], -x[2], -x[3]))

# K번 국가의 등수 구하기
for i in range(N):
    if medals[i][0] == K:
        # 메달 수가 동일한 다른 국가들의 공동 순위를 고려해 처리
        rank = i + 1
        break

print(rank)

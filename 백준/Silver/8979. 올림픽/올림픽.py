# N: 국가의 수, K: 등수를 알고 싶은 국가
N, K = map(int, input().split())

# 각 국가의 메달 정보를 저장할 리스트
countries = []

# N개의 국가 정보 입력 받기
for _ in range(N):
    # country: 국가번호, gold: 금메달, silver: 은메달, bronze: 동메달
    country, gold, silver, bronze = map(int, input().split())
    countries.append([country, gold, silver, bronze])

# K번 국가의 메달 정보 찾기
k_medals = None
for country in countries:
    if country[0] == K:
        k_medals = country[1:]  # 금, 은, 동메달 정보만 저장
        break

# K국가보다 더 잘한 나라의 수를 세기
better_count = 0
for country in countries:
    medals = country[1:]  # 현재 국가의 메달 정보
    
    # 메달 순서대로 비교 (금 -> 은 -> 동)
    if (medals[0] > k_medals[0]) or \
       (medals[0] == k_medals[0] and medals[1] > k_medals[1]) or \
       (medals[0] == k_medals[0] and medals[1] == k_medals[1] and medals[2] > k_medals[2]):
        better_count += 1

# K국가의 등수 = (자신보다 더 잘한 나라 수) + 1
print(better_count + 1)
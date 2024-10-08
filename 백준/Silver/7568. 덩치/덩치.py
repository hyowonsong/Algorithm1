n = int(input())  
people = []  


for _ in range(n):
    x, y = map(int, input().split())
    people.append((x, y))

# 처음에 모든 사람의 덩치 등수를 1로 초기화 (중요!)
rank = [1] * n  

# 각 사람을 비교하여 덩치 등수를 계산
for i in range(n):
    for j in range(n):
        # 자신(i)과 다른 사람(j)을 비교해서 덩치가 더 큰 경우
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank[i] += 1  

# 덩치 등수를 출력 
print(' '.join(map(str, rank)))
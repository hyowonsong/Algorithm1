def dfs(cards, visited, start):
    count = 0
    while not visited[start]:
        visited[start] = True
        start = cards[start] - 1  # 다음 상자의 인덱스
        count += 1
    return count

def solution(cards):
    visited = [False] * len(cards)
    group_sizes = []

    # 모든 상자를 탐색하여 그룹 크기 계산
    for i in range(len(cards)):
        if not visited[i]:
            group_size = dfs(cards, visited, i)
            group_sizes.append(group_size)
    
    # 그룹 크기를 내림차순 정렬
    group_sizes.sort(reverse=True)

    # 점수 계산
    if len(group_sizes) < 2:
        return 0  # 그룹이 하나만 있으면 점수는 0
    else:
        return group_sizes[0] * group_sizes[1]
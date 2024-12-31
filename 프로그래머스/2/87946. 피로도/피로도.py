def dfs(k, dungeons, visited, count):
    # 현재 탐험한 던전 수를 기준으로 최대값 초기화
    max_count = count 

    for i in range(len(dungeons)):
        # 최소 필요 피로도 조건을 만족하면 탐험
        if not visited[i] and k >= dungeons[i][0]:  
            visited[i] = True
            # max_count와 dfs 중 더 큰 것을 선택
            max_count = max(max_count, dfs(k - dungeons[i][1], dungeons, visited, count + 1))
            # 백트래킹 : 다른 경로에서 해당 던전을 다시 탐험할 수 있도록 설정
            visited[i] = False  

    return max_count

def solution(k, dungeons):
    visited = [False] * len(dungeons)  # 던전 방문 여부 저장
    return dfs(k, dungeons, visited, 0)
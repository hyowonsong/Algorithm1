# 피로도

answer = 0  # 최대 던전 클리어 횟수를 저장하는 전역 변수

def dfs(k, cnt, dungeons, visited):
    global answer 
    if cnt > answer:
        answer = cnt  # 현재까지의 클리어 횟수가 최대 클리어 횟수보다 크면 갱신

    for i in range(len(dungeons)):
        # 방문하지 않았고, 현재 피로도로 해당 던전을 클리어할 수 있다면
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True  # 해당 던전을 방문 표시
            dfs(k - dungeons[i][1], cnt + 1, dungeons, visited)  # 재귀적으로 다음 상태 탐색
            visited[i] = False  # 해당 던전 방문 표시를 되돌림

def solution(k, dungeons):
    global answer
    visited = [False] * len(dungeons)
    dfs(k, 0, dungeons, visited)  # 초기 피로도, 클리어 횟수 0, 던전 정보, 방문 여부를 초기값으로 DFS 호출
    return answer  # 최대 던전 클리어 횟수 반환

def check_match(user_id, banned_id):
    # user_id와 banned_id가 길이가 다르면 매칭될 수 없으므로 False 반환
    if len(user_id) != len(banned_id):
        return False
    
    # 각 문자 위치에서 비교
    for i in range(len(user_id)):
        # banned_id의 현재 문자가 '*'가 아니고, 두 문자가 다르면 False 반환
        if banned_id[i] != '*' and banned_id[i] != user_id[i]:
            return False
    # 모든 조건을 만족하면 True 반환
    return True

def dfs(idx, visited, user_id, banned_id, result):
    # banned_id의 모든 조건을 다 검사한 경우
    if idx == len(banned_id):
        # 현재 방문한 user_id들의 조합을 정렬하여 하나의 문자열로 변환
        # 조합의 순서에 관계없이 동일한 조합은 같은 것으로 처리
        current = sorted(list(visited))
        result.add(','.join(current))  # 집합에 저장
        return
    
    # user_id 리스트의 각 사용자에 대해
    for i in range(len(user_id)):
        # 이미 선택된 사용자가 아니고, 매칭 조건을 만족하면
        if user_id[i] not in visited and check_match(user_id[i], banned_id[idx]):
            visited.add(user_id[i])  # 방문 처리
            dfs(idx + 1, visited, user_id, banned_id, result)  # 다음 banned_id 검사
            visited.remove(user_id[i])  # 방문 해제 (백트래킹)

def solution(user_id, banned_id):
    # 결과를 저장할 집합 (중복 조합을 제거하기 위해 사용)
    result = set()
    # DFS 탐색 시작
    dfs(0, set(), user_id, banned_id, result)
    # 가능한 조합의 개수 반환
    return len(result)
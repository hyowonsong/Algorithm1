def check_match(user_id, banned_id):
    if len(user_id) != len(banned_id):
        return False
    
    for i in range(len(user_id)):
        if banned_id[i] != '*' and banned_id[i] != user_id[i]:
            return False
    return True

def dfs(idx, visited, user_id, banned_id, result_set):
    if idx == len(banned_id):
        # 현재까지 선택된 유저들을 정렬하여 문자열로 만들어 저장 
        # 순서와 관계없이 동일한 조합은 같은 것으로 처리하기 위함
        current = sorted(list(visited))
        result_set.add(','.join(current))
        return
    
    for i in range(len(user_id)):
        if user_id[i] not in visited and check_match(user_id[i], banned_id[idx]):
            visited.add(user_id[i])
            dfs(idx + 1, visited, user_id, banned_id, result_set)
            visited.remove(user_id[i])

def solution(user_id, banned_id):
    result_set = set()
    dfs(0, set(), user_id, banned_id, result_set)
    return len(result_set)
def calc_score(apeach, ryan):
    # 어피치와 라이언의 점수 차이 계산
    a_score = 0
    r_score = 0
    
    for i in range(11):
        if apeach[i] == 0 and ryan[i] == 0:
            continue
            
        if apeach[i] >= ryan[i]:
            a_score += (10 - i)
        else:
            r_score += (10 - i)
            
    return r_score - a_score


def is_better(cur, best):
    # 현재 전략이 더 좋은지 확인
    for i in range(10, -1, -1):
        if cur[i] > best[i]:
            return True
            
        if cur[i] < best[i]:
            return False
            
    return False


def dfs(idx, left, cur, best, max_diff, apeach):
    # 최적의 전략 탐색
    if idx == 11 or left == 0:
        if left > 0:
            cur[10] += left
        
        diff = calc_score(apeach, cur)
        
        if diff <= 0:
            if left > 0:
                cur[10] -= left
            return max_diff, best
        
        if diff > max_diff:
            return diff, cur[:]
        
        if diff == max_diff:
            if is_better(cur, best):
                return diff, cur[:]
        
        if left > 0:
            cur[10] -= left
            
        return max_diff, best

    cur[idx] = 0
    max_diff, best = dfs(idx + 1,left,cur,best,max_diff,apeach)

    need = apeach[idx] + 1
    if left >= need:
        cur[idx] = need
        max_diff, best = dfs(idx + 1,left - need,cur,best,max_diff,apeach)
        cur[idx] = 0

    return max_diff, best


def solution(n, info):
    # 라이언의 최적 전략 찾기
    ryan = [0] * 11
    init = [-1]
    
    max_diff, best = dfs(idx=0,left=n,cur=ryan,best=init,max_diff=0,apeach=info)
    
    if max_diff > 0:
        return best
    else:
        return [-1]
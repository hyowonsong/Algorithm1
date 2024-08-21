# 스킬 트리

def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        index = 0
        
        for s in skill_tree:
            if s in skill:
                # 만약 현재 스킬이 올바른 위치에 있으면, index를 증가시키고
                if s == skill[index]:
                    index += 1
                else:
                    # 올바른 위치가 아닌 경우, 해당 스킬트리는 유효하지 않음
                    break
        else:
            # for문을 다 돌았을 때 break 없이 끝나면 유효한 스킬트리
            answer += 1
    
    return answer

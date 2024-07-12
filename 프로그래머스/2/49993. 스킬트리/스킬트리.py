# 스킬트리

def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        # 순서를 index로 정의(이게 제일 중요!) 해주고 valid 도 정의 
        index = 0
        valid = True

        for s in skill_tree:
            if s in skill:
                # 만약 차례대로 안에 있으면 index += 1
                if s == skill[index]:
                    index += 1
                else:
                    valid = False
                    break

        # for 문 다 돌고 valid = True 면 answer += 1 
        if valid:
            answer += 1
        
    return answer
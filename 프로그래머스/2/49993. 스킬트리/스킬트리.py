def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        index = 0
        valid = True  # 유효성을 체크하는 변수

        for s in skill_tree:
            if s in skill:
                # 현재 skill_tree의 skill이 
                # skill의 현재 index 위치의 스킬과 일치해야 함
                if s == skill[index]:
                    index += 1
                else:
                    # 현재 스킬이 skill의 현재 index 위치의 스킬과 다를 때
                    # 올바른 순서가 아니므로 valid를 False로 설정
                    valid = False
                    break
        
        # for 루프를 다 돌고 valid가 True이면 유효한 스킬트리
        if valid:
            answer += 1
    
    return answer

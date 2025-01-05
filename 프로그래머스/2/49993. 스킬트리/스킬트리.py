def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        filter = ""
        
        # skill에 포함된 문자만 순서대로 추출
        for s in skill_tree:
            if s in skill:
                filter += s
        
        # filter가 skill의 앞부분 순서를 따르는지 확인
        is_valid = True
        for i in range(len(filter)):
            if filter[i] != skill[i]:
                is_valid = False
                break
        
        if is_valid:
            answer += 1

    return answer
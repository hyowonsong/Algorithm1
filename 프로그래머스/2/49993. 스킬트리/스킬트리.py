def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        skill_index = 0  # 선행 스킬 순서의 현재 인덱스를 추적
        valid = True

        for s in skill_tree:
            if s in skill:
                if s == skill[skill_index]:
                    skill_index += 1
                else:
                    valid = False
                    break

        if valid:
            answer += 1

    return answer

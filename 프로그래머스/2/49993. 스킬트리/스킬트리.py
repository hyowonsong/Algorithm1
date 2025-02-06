# 스킬트리

def solution(skill, skill_trees):
    answer = 0 

    # skill_trees 안에 있는 것들을 하나씩 반복
    for skill_tree in skill_trees:
        prefix = ""

        # 만약 같은게 있다면 prefix안에 한 단어씩 차례대로 추가 
        for i in skill_tree:
            if i in skill:
                prefix += i

        # 각 prefix 글자의 한 단어씩 돌면서 skill과 같은 순서인지 체크
        is_valid = True
        for i in range(len(prefix)):
            # 만약 같은 순서가 아니면 그 상태에서 False하고 break
            if prefix[i] != skill[i]:
                is_valid = False
                break

        if is_valid:
            answer += 1

    return answer
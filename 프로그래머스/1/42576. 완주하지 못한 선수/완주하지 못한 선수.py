def solution(participant, completion):
    # 참가자 이름과 그 수를 딕셔너리(딕셔너리는 {})
    dict = {}

    for i in participant:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    # 완주자 목록을 순회하면서 참가자 카운트에서 뺍니다.
    for i in completion:
        dict[i] -= 1
        # 카운트가 0이 되면 딕셔너리에서 제거합니다.(이걸 생각)
        if dict[i] == 0:
            del dict[i]

    # 남아있는 참가자가 완주하지 못한 선수입니다.
    for i in dict:
        return i

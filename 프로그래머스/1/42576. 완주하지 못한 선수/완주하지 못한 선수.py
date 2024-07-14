# 완주하지 못한 선수

def solution(participant, completion):
    # 참가자 이름과 그 수를 딕셔너리로 만듭니다.
    participant_count = {}
    for name in participant:
        if name in participant_count:
            participant_count[name] += 1
        else:
            participant_count[name] = 1
    
    # 완주자 목록을 순회하면서 참가자 카운트에서 뺍니다.
    for name in completion:
        participant_count[name] -= 1
        # 카운트가 0이 되면 딕셔너리에서 제거합니다.
        if participant_count[name] == 0:
            del participant_count[name]
    
    # 남아있는 참가자가 완주하지 못한 선수입니다.
    for name in participant_count:
        return name
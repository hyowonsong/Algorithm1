# 음양 더하기

# signs[i] 가 false이면 absolutes[i] 에 있는 값이 -i 가 되어 버린다.
# 문제에서 signs의 값이 참(True)이면 양수, 그렇지 않으면 음수라고 명시되어 있다.
# 따라서 할 필요가 없다.

def solution(absolutes,signs):
    answer = 0
    
    for i in range(len(signs)):
        if signs[i] == True:
            answer += int(absolutes[i])
        else:
            answer -= int(absolutes[i])
    return answer
# 과일 장수

def solution(k,m,score):
    answer= 0
    # reverse는 원본 리스트 자체를 뒤집는다.
    # reversed는 내장 함수로 원본 리스트는 변경되지 않습니다.
    score.sort(reverse=True)

    # m개씩 포장
    for i in range(0,len(score),m):
        if len(score[i:i+m]) == m:
            answer += min(score[i:i+m])*m

    return answer
# 과일 장수

def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)

     # m개씩 나누는거 생각해야지 (for 문 사용)
    for i in range(0, len(score), m):
        # score 길이: len(score) i:i+m 까지가 m 이면 
        if len(score[i:i+m]) == m: 
            answer += min(score[i:i+m])*m
    return answer
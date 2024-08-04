# 자릿수 더하기

def solution(n):
    answer = 0
    # str로 먼저 바꾸기
    new = str(n)
    
    # new의 길이를 for 문 돌리기
    for i in range(len(new)):
        # 여기서 int로 바꾸기 
        answer += int(new[i])
    return answer
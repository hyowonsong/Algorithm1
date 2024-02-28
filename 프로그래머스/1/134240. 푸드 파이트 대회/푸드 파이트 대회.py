def solution(food):
    answer = ""
    for i in range(1, len(food)):
        answer += str(i) * (food[i]//2) # 몫만큼 나눠서 더해준다.
    return answer+str(0)+answer[::-1]
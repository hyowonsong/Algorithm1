def solution(n,a,b):
    answer = 0
    while a != b:                        # 같이 않는 동안 다른 아이들이랑 대결하고 있으니 answer +=1
        answer +=1
        a, b = (a+1)//2, (b+1)//2       # 같다면 같이 대진하고 있는 거니꺼 answer
    return answer
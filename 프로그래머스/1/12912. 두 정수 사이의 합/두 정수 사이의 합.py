# 두 정수 사이의 합

def solution(a,b):
    answer = 0

    if a>b:
        for i in range(b,a+1):
            answer += i

    elif a==b:
        answer = a

    else:
        for i in range(a,b+1):
            answer += i

    return answer

print(solution(3,5))
    
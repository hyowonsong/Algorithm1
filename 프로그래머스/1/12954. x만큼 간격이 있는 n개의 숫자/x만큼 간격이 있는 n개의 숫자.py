def solution(x,n):
    answer = []
    # n+1 을 해줘야 i까지 포함해서 append 해줄 수 있다. 
    # answer +=  이건 안된다! 리스트이기 때문에 int 불가.
    for i in range(1,n+1):
        answer.append(x*i)

    return answer
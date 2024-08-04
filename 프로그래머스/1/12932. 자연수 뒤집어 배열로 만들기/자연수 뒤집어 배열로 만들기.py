
def solution(n):
    answer = []
    new = str(n)        # 12345

    for i in new:
        answer.append(int(i))

    return answer[::-1]
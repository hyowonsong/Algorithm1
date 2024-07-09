# 주식가격

def solution(prices):
    n = len(prices)
    # 배열 초기화
    answer = [0]*n

    for i in range(n):
        for j in range(i+1, n):
            # i가 j보다 크면 가격이 떨어진 것이므로 j-i 만큼의 시간 계산
            if prices[i] > prices[j]:
                answer[i] = j-i
                break
            # 가격이 떨어지지 않은 경우
            elif j == len(prices) - 1:
                answer[i] = j-i

    return answer



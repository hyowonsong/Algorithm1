def solution(begin, end):
    result = []
    for i in range(begin, end + 1):
        result.append(get_max_divisor(i))
    return result

def get_max_divisor(n):
    if n == 1:
        return 0
    max_div = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            div = n // i
            if div <= 10000000:
                return div  # 10,000,000 이하의 가장 큰 약수를 반환
            max_div = max(max_div, i)
    return max_div
def solution(k, d):
    count = 0  
    for x in range(0, d + 1, k):  # x를 k의 배수로 0부터 d까지 반복
        max_y = (d**2 - x**2)**0.5  # 피타고라스 정리 이용
        count += (int(max_y) // k) + 1  # 최대 y를 k로 나눈 몫의 개수에 1을 더해 가능한 y 값 개수를 누적
    return count

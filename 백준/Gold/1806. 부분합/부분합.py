# 부분합

n, s = map(int, input().split())
array = list(map(int, input().split()))

def solution(n, s, array):
    start = 0  # 시작 포인터
    current_sum = 0  # 현재 윈도우의 부분합
    min_length = float('inf')  # 최소 길이를 무한대로 초기화
    

    # `end` 포인터를 사용하여 윈도우를 확장
    for end in range(n):
        current_sum += array[end]  # 윈도우에 새로운 요소를 추가

        # 현재 부분합이 S 이상인 경우 윈도우 축소
        while current_sum >= s:
            min_length = min(min_length, end - start + 1)  # 길이 갱신
            current_sum -= array[start]  # 윈도우에서 시작 요소 제거
            start += 1  # 시작 포인터 이동

    # 결과 출력
    if min_length != float('inf'):
        return min_length  
    else:
        return 0

# 결과 출력
print(solution(n, s, array))

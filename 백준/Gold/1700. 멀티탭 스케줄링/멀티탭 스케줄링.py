import sys

# N: 멀티탭 구멍의 개수, K: 전기 용품의 사용 순서 길이
N, K = map(int, input().split())

# 전기 용품 사용 순서를 리스트로 저장
use = list(map(int, input().split()))

# 멀티탭 코드들을 저장할 리스트
code = []

# 플러그를 뽑은 횟수를 저장할 변수
answer = 0

# 전기 용품 사용 순서에 따라 멀티탭에 꽂는 작업 수행
for i in range(K):
    # 현재 전기 용품이 이미 멀티탭에 꽂혀 있는 경우
    if use[i] in code:
        continue  # 아무 작업도 하지 않고 다음 순서로 넘어감

    # 멀티탭에 빈 자리가 있는 경우
    if len(code) < N:
        code.append(use[i])  # 현재 전기 용품을 멀티탭에 꽂음
        continue  # 다음 순서로 넘어감

    # 멀티탭에 빈 자리가 없고, 꽂혀 있는 플러그를 뽑아야 하는 경우
    priority = []
    for c in code:  # 현재 꽂혀 있는 코드들에 대해
        if c in use[i:]:  # 다음에 또 사용해야 한다면
            priority.append(use[i:].index(c))  # 다음 사용 위치 저장
        else:
            priority.append(101)  # 다시 사용되지 않는 경우 큰 값으로 설정

    # 우선순위가 가장 큰 (가장 늦게 사용되거나 사용되지 않는) 전기 용품 찾기
    target = priority.index(max(priority))

    # 멀티탭에서 해당 전기 용품을 뽑음
    code.remove(code[target])

    # 현재 전기 용품을 멀티탭에 꽂음
    code.append(use[i])

    # 플러그를 뽑은 횟수 증가
    answer += 1

# 플러그를 뽑은 총 횟수를 출력
print(answer)
def dfs(numbers, target, index, current_sum):
    # 종료 조건: 모든 숫자를 탐색했을 때
    if index == len(numbers):
        # 타겟 넘버를 만들었으면 1 반환
        if current_sum == target:
            return True
        else:
            return False

    # 현재 숫자를 더하거나 뺀 두 가지 경우로 재귀 호출
    return dfs(numbers, target, index + 1, current_sum + numbers[index]) + dfs(numbers, target, index + 1, current_sum - numbers[index])

def solution(numbers, target):
    # 초기 DFS 탐색 시작
    return dfs(numbers, target, 0, 0)
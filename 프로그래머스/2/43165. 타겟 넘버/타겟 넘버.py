def solution(numbers, target):
    # DFS를 사용하여 가능한 모든 경우를 탐색
    def dfs(index, current_sum):
        # 모든 숫자를 다 사용했을 때
        if index == len(numbers):
            # 현재 합이 타겟 넘버와 같으면 1을 반환
            if current_sum == target:
                return 1  
            else:
                return 0
        else:
            # 다음 숫자를 더하거나 빼는 두 가지 경우로 나누어 재귀 호출
            return dfs(index + 1, current_sum + numbers[index]) + dfs(index + 1, current_sum - numbers[index])

    # DFS 탐색 시작
    return dfs(0, 0)
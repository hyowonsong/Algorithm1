def dfs(numbers, target, index, current_sum):
    # 모든 숫자를 다 사용했을 때
    if index == len(numbers):
        # 현재 합이 타겟 넘버와 같으면 1을 반환
        if current_sum == target:
            return 1  
        else:
            return 0
    else:
        # 다음 숫자를 더하는 경우
        add_case = dfs(numbers, target, index + 1, current_sum + numbers[index])
        
        # 다음 숫자를 빼는 경우
        subtract_case = dfs(numbers, target, index + 1, current_sum - numbers[index])
        
        # 두 경우의 결과를 더해 반환
        return add_case + subtract_case

def solution(numbers, target):
    # DFS 탐색 시작
    return dfs(numbers, target, 0, 0)

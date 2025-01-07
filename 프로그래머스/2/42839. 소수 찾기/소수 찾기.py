# 소수 찾기

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def dfs(numbers, current, visited, results):
    # numbers: 숫자 문자열
    # current: 현재까지 조합된 숫자
    # visited: 방문 여부를 기록한 리스트
    # results: 생성된 숫자 조합을 저장할 집합
    if current:
        results.add(int(current))  # 현재 조합을 정수로 변환하여 저장

    for i in range(len(numbers)):
        if not visited[i]:  # 방문하지 않은 숫자만 추가
            visited[i] = True
            dfs(numbers, current + numbers[i], visited, results)
            visited[i] = False  # 백트래킹

def solution(numbers):
    results = set()  # 중복 제거를 위해 집합 사용
    visited = [False] * len(numbers)  # 방문 여부 초기화
    dfs(numbers, "", visited, results)
    
    # 소수 개수 세기
    count = 0
    for num in results:
        if is_prime(num):
            count += 1
    
    return count

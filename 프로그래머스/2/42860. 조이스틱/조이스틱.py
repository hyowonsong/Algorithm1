def solution(name):
    # 특정 문자를 'A'에서 목표 문자로 바꾸는 최소 횟수를 계산
    def cost(c):
        # ord(c) - ord('A'): 문자를 'A'에서 c까지 위쪽으로 조작하는 횟수입니다.
        # 26 - (ord(c) - ord('A')): 위쪽보다 아래쪽으로 조작할 경우의 횟수입니다.
        # 두 값을 비교하여 더 적은 조작 횟수를 반환
        return min(ord(c) - ord('A'), 26 - (ord(c) - ord('A')))
    
    # 각 문자에 대한 변경 비용 계산
    move = 0
    for c in name:
        move += cost(c)
    
    n = len(name)  # 문자열 길이
    min_mv = n - 1  # 최소 커서 이동 횟수 (오른쪽으로 끝까지 이동하는 경우)
    
    # 커서 이동 최적화 계산
    for i in range(n):
        # 현재 위치 i에서 연속된 'A'가 있는지 확인합니다.
        # j는 i + 1에서 시작하며, 연속된 'A'의 끝까지 증가합니다.
        j = i + 1
        while j < n and name[j] == 'A':  
            j += 1
        
        # 앞에서 돌아가기 vs 끝까지 가서 돌아오기 비교
        # i: 처음부터 현재 위치까지의 거리 (왼쪽 방향)
        # n - j: 마지막 위치에서 연속된 'A'가 끝나는 위치까지의 거리 (오른쪽 방향)
        # 두 값 중 더 작은 값을 선택하여 효율적인 이동 경로를 결정
        dist = min(i, n - j)  
        # 최소 이동 횟수를 업데이트
        # 현재 위치까지 이동한 후 뒤로 돌아가는 거리(i + n - j + dist)를 고려하여 최적의 값으로 갱신
        min_mv = min(min_mv, i + n - j + dist)
    
    # 문자 변경 횟수(move)와 커서 이동 최소 횟수(min_mv)를 더해 최종 최소 조작 횟수를 반환
    return move + min_mv  
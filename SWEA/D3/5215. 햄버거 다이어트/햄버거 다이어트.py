T = int(input())

for t in range(1, T + 1):
    # N: 재료의 수, L: 제한 칼로리
    N, L = map(int, input().split())
    
    # 각 재료의 점수와 칼로리 저장
    ingredients = []
    
    for i in range(N):
        # T: 맛 점수, K: 칼로리
        T, K = map(int, input().split())  
        ingredients.append((T, K))
    
    # dp 배열: dp[i]는 i 칼로리 이하로 구성한 조합에서의 최대 맛 점수
    dp = [0] * (L + 1)
    
    # 재료들을 하나씩 확인
    for taste, cal in ingredients:
        # 현재 재료를 사용할 수 있는 칼로리 제한 내에서 반영
        # 높은 칼로리부터 계산해야 같은 재료를 여러 번 선택하지 않음
        for current_cal in range(L, cal - 1, -1):
            # dp 배열을 업데이트 (현재 재료를 포함한 경우)
            dp[current_cal] = max(dp[current_cal], dp[current_cal - cal] + taste)
    
    # 결과 출력
    print(f'#{t} {max(dp)}')
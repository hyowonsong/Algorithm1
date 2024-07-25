def solution(sticker):
    n = len(sticker)
    if n == 1:
        return sticker[0]  # 스티커가 하나만 있는 경우, 그 스티커의 값 반환
    
    # 첫 번째 스티커를 포함하는 경우
    dp1 = [0] * n
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    for i in range(2, n-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])
    
    # 첫 번째 스티커를 포함하지 않는 경우
    dp2 = [0] * n
    dp2[1] = sticker[1]
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])
    
    # 두 경우의 최대값 반환
    return max(dp1[n-2], dp2[n-1])

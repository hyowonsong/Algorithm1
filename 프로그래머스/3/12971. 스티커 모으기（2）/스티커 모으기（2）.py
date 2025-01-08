def solution(sticker):
    n = len(sticker)
    
    # 스티커가 하나만 있는 경우, 그 스티커의 값 반환
    if n == 1:
        return sticker[0] 
    
    # 첫 번째 스티커를 포함하는 경우 dp1을 업데이트
    dp1 = [0] * n
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    # 이 경우 첫 번째 스티커를 뜯었다고 가정하니 마지막 스티커는 사용 X
    for i in range(2, n-1):
        # dp1[i-1]: 이전 스티커까지의 최대합. 현재 스티커는 포함하지 않음.
        # dp1[i-2] + sticker[i]:두 칸 전까지의 최대합에 현재 스티커를 포함
        # 위 두 값 중 더 큰 값을 선택
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])
    
    # 첫 번째 스티커를 포함하지 않는 경우 dp2를 업데이트
    dp2 = [0] * n
    dp2[1] = sticker[1]
    # 첫 번째 스티커를 뜯지 않았으므로, 마지막 스티커를 포함
    for i in range(2, n):
        # dp2[i-1]: 이전 스티커까지의 최대합. 현재 스티커는 포함하지 않음
        # dp2[i-2] + sticker[i]: 두 칸 전까지의 최대합에 현재 스티커를 포함
        # 위 두 값 중 더 큰 값을 선택.
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])
    
    # 두 경우 중 최대값 반환
    return max(dp1[n-2], dp2[n-1])

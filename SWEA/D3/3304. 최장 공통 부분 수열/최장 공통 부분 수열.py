# 테스트 케이스 수 입력
T = int(input())

for t in range(1, T + 1):
    # 두 문자열 입력
    str1, str2 = input().split()

    # 두 문자열의 길이
    len1 = len(str1)
    len2 = len(str2)

    # DP 테이블 생성 및 초기화
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # DP 테이블을 채우기
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            # 0 기반 인덱스이므로 1을 빼줍니다
            # 문자가 같으면
            if str1[i - 1] == str2[j - 1]:  
                # dp[i - 1][j - 1]에서 가져와 1을 더하여 현재 dp[i][j]에 저장
                dp[i][j] = dp[i - 1][j - 1] + 1
            # 문자가 다르면
            else:  
                # dp[i - 1][j]와 dp[i][j - 1] 중 큰 값으로 설정
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # LCS 길이
    result = dp[len1][len2]
    
    # 결과 출력
    print(f"#{t} {result}")
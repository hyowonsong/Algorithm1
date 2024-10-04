T = int(input())
for test_case in range(1, T + 1):
    # N: 문자열 개수, M: 각 문자열의 길이
    N, M = map(int, input().split())
    # 모든 문자열 입력 받기
    word = [input() for _ in range(N)]
    
    # 각 유형별 문자열 개수 카운트
    half_pal = 0  # 쌍을 이루는 문자열 개수
    pal = 0       # 팰린드롬 문자열 개수
    nothing = 0   # 사용할 수 없는 문자열 개수
    
    # 모든 문자열을 분류할 때까지 반복
    while half_pal + pal + nothing != N:
        # 현재 문자열이 팰린드롬인 경우
        if word[0] == word[0][::-1]:
            pal += 1
            word.pop(0)
        # 현재 문자열의 역순이 나머지 문자열 중에 있는 경우
        elif word[0][::-1] in word[1:]:
            index = word[1:].index(word[0][::-1])
            half_pal += 2
            word.pop(0)
            word.pop(index)
        # 사용할 수 없는 문자열인 경우
        else:
            nothing += 1
            word.pop(0)
    
    # 최종 팰린드롬 길이 계산
    result = half_pal * M  # 쌍을 이루는 문자열들의 총 길이
    if pal > 0:  # 팰린드롬이 하나라도 있으면 가운데 배치
        result += M
        
    print(f"#{test_case} {result}")
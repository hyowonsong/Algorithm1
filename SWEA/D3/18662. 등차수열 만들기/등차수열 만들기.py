T = int(input())

for tc in range(T):
    a, b, c = map(int, input().split())

    result = 0
    if a + c == 2 * b:  # 이미 등차수열을 이루는 경우
        print(f"#{tc+1} {0.0}")
    else:
        # 등차수열이 아닌 경우 가장 작은 x 값을 계산
        if 2 * b > a + c:
            result = (2 * b) - (a + c)
            result /= 2
        elif 2 * b < a + c:
            result = (a + c) - (2 * b)
            result /= 2
        print(f"#{tc+1} {result:.1f}")

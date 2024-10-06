# 정답 코드

s = input()

# 입력된 문자열의 길이가 짝수인 경우에만 진행
if len(s) % 2 == 0:
    middle = len(s) // 2  # 문자열의 중간 인덱스 계산
    left_sum = sum(map(int, s[:middle]))  # 왼쪽 부분의 숫자 합 계산
    right_sum = sum(map(int, s[middle:]))  # 오른쪽 부분의 숫자 합 계산

    # 왼쪽 부분의 숫자 합과 오른쪽 부분의 숫자 합이 동일한 경우
    if left_sum == right_sum:
        print("LUCKY")
    else:
        print("READY")
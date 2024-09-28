# 숫자 1부터 순서대로 말하되 3,6,9 가 들어가 있는 수는 말하지X

N = int(input())

for i in range(1, N+1):
    count = 0
    str_i = str(i)

    for char in str_i:
        if char == '3' or char == '6' or char == '9':
            count += 1

    # 박수 횟수가 1이상이면 박수, 아니면 숫자 출력
    if count>0:
        print('-' * count, end=' ')  # 박수 횟수만큼 '-' 출력
    else:
        print(i, end=' ')
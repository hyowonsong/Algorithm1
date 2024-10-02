T = 10
for t in range(1, T+1):
    legnth, password = input().split()

    answer = []

    for i in password:
        if len(answer) > 0 and answer[-1] == i:
            answer.pop()
        else:
            answer.append(i)

    a = ''.join(answer)
    print(f'#{t} {a}')

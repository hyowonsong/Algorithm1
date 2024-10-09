# 한 줄로 서기

n = int(input())
arr = list(map(int, input().split()))
answer = [0] * n

# 한명씩 순회
for i in range(n):
    # 현재 사람보다 큰 사람이 왼쪽에 몇 명 배치되었는지 카운트
    cnt = 0
    # 각 자리를 순차적으로 확인
    for j in range(n):
        # 왼쪽에 큰 사람의 수가 맞고 현재 자리가 비어있다면
        if cnt == arr[i] and answer[j] == 0:
            # 해당 자리에 현재 사람을 배치
            answer[j] = i+1
            break

        # 자리가 비어있으면(아직 사람을 배치하지 않은 자리)
        elif answer[j] == 0:
            # 큰 사람의 수를 증가
            cnt += 1

print(' '.join(map(str,answer)))

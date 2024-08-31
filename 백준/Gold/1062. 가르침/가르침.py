# 입력 받기
n, k = map(int, input().split())

# k가 5보다 작으면 어떤 언어도 배울 수 없음
if k < 5:
    print(0)
    exit()

# k가 26이면 모든 알파벳을 배울 수 있으므로 모든 단어를 읽을 수 있음
elif k == 26:
    print(n)
    exit()

words = []
required = {'a', 'c', 'i', 'n', 't'}  # 기본적으로 배워야 하는 알파벳

# 각 단어에서 기본적으로 배워야 하는 알파벳을 제외한 알파벳만 저장
for _ in range(n):
    word = set(input().rstrip()) - required
    words.append(word)

# 학습된 알파벳을 비트마스크로 표현
learn = 0
for c in required:
    learn |= (1 << (ord(c) - ord('a')))

# DFS를 비트마스킹으로 변형
def dfs(idx, cnt, learn):
    global answer

    # k개의 알파벳을 모두 학습한 경우
    if cnt == k:
        readcnt = 0
        for word in words:
            can_read = True
            for c in word:
                if not (learn & (1 << (ord(c) - ord('a')))):
                    can_read = False
                    break
            if can_read:
                readcnt += 1
        answer = max(answer, readcnt)
        return

    # 가능한 알파벳을 선택
    for i in range(idx, 26):
        if not (learn & (1 << i)):
            dfs(i + 1, cnt + 1, learn | (1 << i))

answer = 0

# DFS 탐색 시작
dfs(0, 5, learn)

# 최종 결과 출력
print(answer)

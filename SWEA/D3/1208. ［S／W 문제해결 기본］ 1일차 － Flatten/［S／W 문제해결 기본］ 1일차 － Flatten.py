# Flatten

T = 10
for test_case in range(1,T+1):
    N = int(input())
    # 계속 최저에 한개씩 넣어주고 다시 최저를 찾아서 구하기 
    lst = list(map(int, input().split()))
    ans = 100
    for _ in range(N):
        lst.sort()
        lst[0] += 1
        lst[-1] -= 1
        if ans> max(lst)-min(lst):
            ans = max(lst)-min(lst)
    print(f'#{test_case} {ans}')
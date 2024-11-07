# 정식이의 은행업무

def solve():
    for i in range(len(lst2)):
        # 계속 하나씩 바꿔준다
        lst2[i] = (lst2[i]+1)%2
        # [1] 2진수 -> 10진수 (num을 계속해서 더해간다)
        num = 0
        for n in lst2:
            num = num*2 + n
 
        # [2] 10 -> 3진수
        conv3, t = [], num
        while t > 0:
            # t를 3으로 나누고 남은 것은 conv3 리스트의 맨 앞에 추가
            conv3.insert(0, t % 3)
            # 다시 t를 3으로 나눠버림
            t //= 3
 
        # [3] 주어진 3진수와 변환된 3진수 비교
        r1, r2, cnt = conv3[::-1], lst3[::-1], 0
        for j in range(min(len(r1), len(r2))):
            if r1[j]!=r2[j]:
                cnt += 1
        cnt += abs(len(r1)-len(r2))
        if cnt==1:
            return num
 
        lst2[i] = (lst2[i]+1)%2    # 원상복구
 
 
T = int(input())
# T = 10
for test_case in range(1, T + 1):
    lst2 = list(map(int, input()))
    lst3 = list(map(int, input()))
 
    ans = solve()
    print(f'#{test_case} {ans}')
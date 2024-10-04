
T = int(input())

planet = {
    0: "ZRO",
    1: "ONE",
    2: "TWO",
    3: "THR",
    4: "FOR",
    5: "FIV",
    6: "SIX",
    7: "SVN",
    8: "EGT",
    9: "NIN"
}


for t in range(T):
    tc_len = input().split()

    lst = input().split()

    # 각 숫자의 개수를 저장할 리스트
    ans = []

    # 0부터 9까지 반복하여 각 숫자의 개수 세기
    for i in range(10):
        count = lst.count(planet[i])
        ans.append(count)

    print(f"#{t + 1}")
    for i in range(10):
        print((planet[i] + " ") * ans[i], end="")
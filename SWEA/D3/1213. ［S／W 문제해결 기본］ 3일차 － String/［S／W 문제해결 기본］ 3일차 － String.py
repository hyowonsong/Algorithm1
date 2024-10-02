T = 10

for t in range(1,T+1):
    T = int(input())
    search = input()
    str_all = input()

    ans = str_all.count(search)

    print(f"#{t} {ans}")

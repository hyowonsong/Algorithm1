T = int(input())

for t in range(1, T + 1):
    N = int(input())
    s = ""
    
    for _ in range(N):
        a, n = input().split()
        s += a * int(n)
    
    print(f"#{t}")
    
    for i in range(0, len(s), 10):
        print(s[i:min(i+10, len(s))])
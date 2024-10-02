T = int(input())
for t in range(1, T + 1):
    p,q,r,s,w = map(int,input().split())

    a = p*w
    b = 0

    if r >= w:
        b = q
    else:
        b = (w-r)*s+q
        
    print(f"#{t} {min(a,b)}")
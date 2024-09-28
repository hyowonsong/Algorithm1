A, B = map(int, input().split())

if (A == 1 and B == 3) or (A == 2 and B == 1) or (A == 3 and B == 2):
    print("A")  # A가 이기는 경우
else:
    print("B")  # B가 이기는 경우
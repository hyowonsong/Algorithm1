T = int(input())  

for t in range(1, T + 1):
    N = int(input())  
    cards = input().split()  

    # 덱을 두 부분으로 나누기
    half = (N + 1) // 2  
    first_half = cards[:half]  
    second_half = cards[half:] 

    # 셔플된 카드 덱
    shuffled = []  
    for i in range(half):
        # 첫 번째 절반 카드 추가
        shuffled.append(first_half[i])  
        # 두 번째 절반이 있는 경우
        if i < len(second_half):  
            # 두 번째 절반 카드 추가
            shuffled.append(second_half[i])  

    print(f"#{t} {' '.join(shuffled)}")  
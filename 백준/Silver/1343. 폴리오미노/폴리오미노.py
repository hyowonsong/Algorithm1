String = input()  

prepared = ''  
String = String.split('.') 

# 나뉜 각 부분에 대해 처리
for part in String:
    length = len(part)  # 각 부분의 길이를 계산
    if length % 2 != 0:  # 길이가 홀수이면 덮을 수 없으므로 -1 출력 후 종료
        print(-1)
        exit()

    # AAAA로 덮을 수 있는 만큼 덮고, 남은 부분은 BB로 덮음
    prepared += 'AAAA' * (length // 4)
    prepared += 'BB' * ((length % 4) // 2)

    # 각 폴리오미노를 덮고 나서 원래 '.'이 있던 위치에 다시 '.'을 추가
    prepared += '.'

# 마지막에 붙은 '.' 제거 후 출력
print(prepared[:-1])
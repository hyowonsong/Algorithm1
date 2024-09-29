# 회문1
# 가로 세로 돌아다니면서 회문 같은거 출력하기

T = 10 
for t in range(1, T + 1):
    length = int(input().strip())  
    board = [input().strip() for _ in range(8)] 

    # 회문 개수 초기화
    count = 0  

    # 가로에서 회문 검사
    for i in range(8):
        for j in range(8 - length + 1):
            substring = board[i][j:j + length]
            if substring == substring[::-1]:  # 회문 확인
                count += 1

    # 세로에서 회문 검사
    for j in range(8):
        for i in range(8 - length + 1):
            substring = ''  # 세로 문자열을 저장할 변수 초기화
            
            # 세로로 문자열을 구성
            for k in range(length):  # 길이 만큼 반복
                substring += board[i + k][j]  # 현재 열의 (i + k) 행에서 문자 추가

            # 회문 확인
            if substring == substring[::-1]:  # 회문인지 확인
                count += 1  # 회문이면 카운트 증가

    print(f'#{t} {count}')  # 결과 출력
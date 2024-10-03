T = 10  

for t in range(1, T+1):
    # 암호문 개수 입력
    N = int(input())
    # 원본 암호문 리스트로 입력
    pwd = list(map(int, input().split()))
    # 명령어 개수 입력
    M = int(input())
    # 명령어 처리
    commands = list(input().split())

    i = 0
    while i < len(commands):
        # 삽입 명령어 처리
        if commands[i] == 'I':  
            x = int(commands[i+1])  # 삽입 위치
            y = int(commands[i+2])  # 삽입할 암호문의 수
            s = list(map(int, commands[i+3:i+3+y]))  # 삽입할 암호문들
            # x번째 다음 위치에 s 리스트 삽입
            pwd[x:x] = s  # 리스트 슬라이싱으로 삽입
            i += 3 + y  # 명령어 크기만큼 건너뜀

        # 삭제 명령어 처리
        elif commands[i] == 'D':  
            x = int(commands[i+1])  # 삭제 시작 위치
            y = int(commands[i+2])  # 삭제할 암호문의 수
            # x번째 다음부터 y개의 암호문 삭제
            del pwd[x:x+y]
            i += 3  # 명령어 크기만큼 건너뜀

         # 추가 명령어 처리
        elif commands[i] == 'A': 
            y = int(commands[i+1])  # 추가할 암호문의 수
            s = list(map(int, commands[i+2:i+2+y]))  # 추가할 암호문들
            pwd.extend(s)  # 리스트 뒤에 암호문 추가
            i += 2 + y  # 명령어 크기만큼 건너뜀

    # (처음 10개만)
    print(f"#{t}", ' '.join(map(str, pwd[:10])))
T = 10  

for _ in range(T):
    n = int(input())
    
    graph = [input().strip() for _ in range(100)]
    
    # 가장 긴 회문의 길이
    max_length = 1

    # 가로 회문 길이 찾기
    for i in range(100):
        for start in range(100):
            for end in range(start + 1, 101):
                substring = graph[i][start:end]
                
                # 회문인지 확인
                if substring == substring[::-1]:
                    max_length = max(max_length, len(substring))

    # 세로 회문 길이 찾기
    for j in range(100):
        for start in range(100):
            for end in range(start + 1, 101):
                # 세로 문자열 추출
                substring = '' 
                for i in range(start, end):
                    # 각 i 번째 행의 j 번째 열에서 글자를 추출하여 추가
                    substring += graph[i][j]  

                # 회문인지 확인
                if substring == substring[::-1]:
                    max_length = max(max_length, len(substring))

    print(f'#{n} {max_length}')
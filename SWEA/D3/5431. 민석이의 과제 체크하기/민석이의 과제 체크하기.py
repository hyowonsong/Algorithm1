T = int(input())  

for t in range(1, T + 1):
    N, K = map(int, input().split())  # N: 수강생 수, K: 과제 제출한 사람 수
    submitted = list(map(int, input().split()))  # 제출한 사람들의 번호
    
    not_submitted = []  # 제출하지 않은 사람들의 번호를 저장할 리스트

    for i in range(1, N + 1):  # 1부터 N까지 반복
        if i not in submitted:  # i가 제출한 사람들 리스트에 없으면
            not_submitted.append(i)  # not_submitted 리스트에 추가

    # 결과 출력
    print(f'#{t}', *not_submitted)
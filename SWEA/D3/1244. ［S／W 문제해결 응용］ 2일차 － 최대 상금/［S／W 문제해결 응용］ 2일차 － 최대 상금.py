# 최대 상금

# n은 현재까지 교환이 몇 번 이루어졌는지 나타내는 변수
def dfs(n): 
    # 최대 상금을 저장할 전역 변수 ans 사용
    global ans  
    # 교환 횟수 N번이 모두 완료되었으면
    if n == N:  
        # 현재 숫자 상태를 기준으로 최대 상금 갱신
        ans = max(ans, int("".join(map(str, lst)))) 
        return 
    
    # lst에서 두 개의 숫자를 교환하는 모든 경우를 탐색
    for i in range(L - 1):  
        for j in range(i + 1, L):  
            lst[i], lst[j] = lst[j], lst[i]  

            # 현재 숫자 상태와 교환 횟수를 결합하여 고유값 생성
            chk = int("".join(map(str, lst))) * 10 + n  

            # 이 상태가 처음이면
            if chk not in v:
                # 다음 교환을 진행 (재귀 호출)  
                dfs(n + 1)  
                # 이 상태를 기록하여 중복 방지
                v.append(chk)  

            # 원래 상태로 되돌리기 (백트래킹)
            lst[i], lst[j] = lst[j], lst[i]  
 
T = int(input())  
for test_case in range(1, T + 1):
    # st는 숫자판 정보, t는 교환 횟수
    st, t = input().split() 
    # 교환 횟수를 정수로 변환
    N = int(t)
    # 숫자판을 정수 리스트로 변환
    lst = [int(ch) for ch in st] 
    # 숫자판의 길이 (자리 수) 
    L = len(lst)  
    # 결과값 초기화 (최대 상금)
    ans = 0 
    # 중복 탐색을 방지하기 위한 리스트
    v = [] 
    # DFS 탐색 시작 (n=0부터 시작) 
    dfs(0) 
    print(f'#{test_case} {ans}')  

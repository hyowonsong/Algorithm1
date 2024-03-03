# H-Index
# 리스트 n번째 값이 최초로 n을 넘지 않을 때, n-1의 값이 H-Index 값이 됩니다.

def solution(citations):
    answer = 0
    citations.sort(reverse=True)    # 내림차순으로 정렬
    
    for i in range(len(citations)):
        if(citations[i] < i+1):     # H-Index 값을 구하기위해 비교(i는 0부터 시작하니 i+1이랑 비교)
             return i
    return len(citations)                     # 인용 횟수가 모두 같을때는 전체를 return
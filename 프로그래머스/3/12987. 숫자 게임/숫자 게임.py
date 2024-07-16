# B의 가장 큰 숫자가 A의 가장 큰 숫자를 이기는 선택

def solution(A, B):
    A.sort()
    B.sort()
    
    a_idx = 0
    b_idx = 0
    answer = 0
    
    while b_idx < len(B) and a_idx < len(A):
        if B[b_idx] > A[a_idx]:
            answer += 1
            a_idx += 1
        b_idx += 1
        
    return answer

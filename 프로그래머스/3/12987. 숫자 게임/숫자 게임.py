def solution(A, B):
    # A와 B를 정렬
    A.sort()
    B.sort()

    # 두 포인터 초기화
    a_idx = 0
    b_idx = 0
    score = 0

    # 두 배열을 비교하며 승점 계산
    while a_idx < len(A) and b_idx < len(B):
        if B[b_idx] > A[a_idx]:  # B팀의 숫자가 A팀의 숫자보다 크면 승리
            score += 1
            a_idx += 1  # A팀의 다음 선수
            b_idx += 1  # B팀의 다음 선수
        else:
            b_idx += 1  # B팀의 숫자가 작거나 같으면 다음 B팀 선수로 이동

    return score
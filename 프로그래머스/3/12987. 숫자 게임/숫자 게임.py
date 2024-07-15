def solution(A, B):
    B.sort(reverse=True)  # B팀의 숫자들을 내림차순으로 정렬
    b_index = 0  # B팀의 현재 인덱스
    score = 0  # B팀의 점수

    for a in sorted(A, reverse=True):  # A팀의 숫자들도 내림차순으로 정렬
        if B[b_index] > a:
            score += 1  # 점수를 증가
            b_index += 1  # 다음 B팀 숫자로 이동
        
        if b_index == len(B):
            break  # 모든 B팀 숫자를 사용했다면 종료

    return score
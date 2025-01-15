# 연속 펄스 부분 수열의 합

def solution(sequence):
    n = len(sequence)
    
    # 펄스 수열 생성 
    pulse1 = [0] * n  # 크기 n의 리스트를 0으로 초기화
    pulse2 = [0] * n  # 크기 n의 리스트를 0으로 초기화
    
    for i in range(n):
        if i % 2 == 0:
            pulse1[i] = 1  # 1, -1, 1, -1, ...
            pulse2[i] = -1  # -1, 1, -1, 1, ...
        else:
            pulse1[i] = -1
            pulse2[i] = 1
    
    # 펄스 수열과 곱한 결과
    seq1 = [sequence[i] * pulse1[i] for i in range(n)]
    seq2 = [sequence[i] * pulse2[i] for i in range(n)]
    
    # 최대 부분 합 계산 
    def max_sub_sum(arr):
        max_sum = arr[0]
        current_sum = arr[0]
        for x in arr[1:]:
            current_sum = max(x, current_sum + x)  # 현재 합 업데이트
            max_sum = max(max_sum, current_sum)  # 최대 합 갱신
        return max_sum
    
    # 각각의 최대 부분 합
    max_sum1 = max_sub_sum(seq1)
    max_sum2 = max_sub_sum(seq2)
    
    # 두 값 중 더 큰 값 반환
    return max(max_sum1, max_sum2)
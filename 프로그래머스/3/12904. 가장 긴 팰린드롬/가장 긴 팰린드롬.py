
def solution(s):
    # 문자열의 길이가 1보다 작거나 문자열이 이미 팰린드롬이면 그대로 길이를 반환
    if len(s) < 2 or s == s[::-1]:
        return len(s)
    
    # 팰린드롬을 확장하여 찾는 함수
    def expand(left, right):
        # left와 right가 문자열의 범위 내에 있고, 두 문자가 같으면 팰린드롬 확장
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1   # 왼쪽으로 한 칸 이동
            right += 1  # 오른쪽으로 한 칸 이동
        # 확장한 범위에서 팰린드롬의 길이 계산 (left와 right는 각각 더 이상 팰린드롬이 아닌 문자를 가리키므로, -1 해준다)
        return right - left - 1
    
    # 가장 긴 팰린드롬의 길이를 저장하는 변수
    max_length = 1
    
    # 문자열의 모든 문자에 대해 팰린드롬을 확장하며 최대 길이를 찾기
    for i in range(len(s)-1):
        # 홀수 길이 팰린드롬 검사 (중심을 한 문자로)
        max_length = max(max_length, expand(i, i))
        # 짝수 길이 팰린드롬 검사 (중심을 두 문자로)
        max_length = max(max_length, expand(i, i+1))
    
    # 최종적으로 찾은 가장 긴 팰린드롬의 길이를 반환
    return max_length
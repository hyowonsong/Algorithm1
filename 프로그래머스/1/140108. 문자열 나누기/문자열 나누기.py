def solution(s):
    count = 0
    while s:
        x = s[0]
        count_x = 0
        count_not_x = 0
        for i in range(len(s)):
            if s[i] == x:
                count_x += 1
            else:
                count_not_x += 1
            # x와 x가 아닌 글자의 개수가 같아지는 순간
            if count_x == count_not_x:
                count += 1
                s = s[i+1:]  # 분리된 부분을 제거하고 남은 부분만 다시 처리
                break
        else:
            # 더 이상 읽을 글자가 없는 경우
            count += 1
            break
    
    return count
# 옹알이(2)

def solution(babbling):
    answer = 0  
    speak = ['aya', 'ye', 'woo', 'ma']  
    
    # babbling과 speak 둘다 같이 for 문 돌리고 j가 bab에 없다면
    for bab in babbling:
        # 각 단어에 대해 처리
        for j in speak:
            # 연속된 같은 발음이 없을 때만 발음을 빈 문자열로 대체
            if j*2 not in bab:
                bab = bab.replace(j,' ')
                
        # 공백만 남았으면 조건에 맞는 단어로 간주
        if bab.isspace():
            answer += 1
            
    return answer  # 조건을 만족하는 단어의 개수를 반환

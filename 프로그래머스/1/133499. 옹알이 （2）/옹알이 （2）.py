# 옹알이

def solution(babbling):
    answer = 0
    speak = ['aya', 'ye', 'woo', 'ma']
    
    for bab in babbling:
        for j in speak:
            if j*2 not in bab:
                bab = bab.replace(j,' ')
                
        if bab.isspace():
            answer +=1
            
    return answer
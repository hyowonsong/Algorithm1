# 포켓몬
# 전체에서 반 만 뽑고 최대로 많이 뽑을 수 있은거 출력

def solution(nums):
    answer = 0
    pokemon = len(nums)//2
    nums = set(nums)
        
    answer = min(len(nums), pokemon)
    
    
    return answer


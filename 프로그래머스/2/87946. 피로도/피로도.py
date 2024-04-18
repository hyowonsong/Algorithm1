
from itertools import permutations

def solution(k, dungeons):
    max_dungeons = 0
    
    # 던전들의 순서를 모두 조합하여 확인
    for perm in permutations(dungeons):
        current_fatigue = k
        count = 0
        
        for dungeon in perm:
            min_fatigue, consume_fatigue = dungeon
            # 현재 피로도로 해당 던전을 탐험할 수 있는지 확인
            if current_fatigue >= min_fatigue:
                count += 1
                current_fatigue -= consume_fatigue
                
        # 최대 던전 수 업데이트
        max_dungeons = max(max_dungeons, count)
    
    return max_dungeons

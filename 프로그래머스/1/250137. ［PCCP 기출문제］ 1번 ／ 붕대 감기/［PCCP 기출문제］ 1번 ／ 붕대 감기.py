# 붕대 감기

# t초 동안 붕대를 감으면서 1초마다 x만큼의 체력을 회복
# t초 연속으로 붕대를 감는 데 성공한다면 y만큼의 체력을 추가로 회복
# 게임 캐릭터에는 최대 체력이 존재해 현재 체력이 최대 체력보다 커지는 것은 불가능

# 붕대 감기를 쓰는 도중 몬스터에게 공격을 당하면 기술이 취소 됨
# 몬스터에게 공격을 당해 기술이 취소 or 기술이 끝나면 그 즉시 다시 사용

# 몬스터의 공격을 받으면 정해진 피해량만큼 체력이 줄어들고 0이하가 되면 죽음

# [입력값]
# 1. bandage : 기술의 시전 시간, 1초당 회복량, 추가 회복량 y를 담은 1차원 배열
# 2. health : 최대 체력
# 3. attacks : 몬스터의 공격 시간과 피해량

# 모든 공격이 끝난 직후 남은 체력을 return 
# 체력이 0이하가 되어 죽는다면 -1을 return

def solution(bandage, health, attacks):
    t, x, y = bandage  # 시전 시간, 초당 회복량, 추가 회복량
    max_health = health  # 최대 체력 저장
    current_health = health  # 현재 체력
    
    # attacks를 딕셔너리로 변환하여 빠른 검색 가능하게 함
    attack_dict = {}
    for attack in attacks:
        time = attack[0]
        damage = attack[1]
        attack_dict[time] = damage
    
    last_attack_time = attacks[-1][0]  # 마지막 공격 시간
    
    consecutive_healing = 0  # 연속 힐링 시간
    
    # 처음부터 마지막 공격 시간까지 시뮬레이션
    for current_time in range(1, last_attack_time + 1):
        # 공격이 있는 시간인 경우
        if current_time in attack_dict:
            damage = attack_dict[current_time]
            current_health -= damage
            consecutive_healing = 0  # 연속 힐링 초기화
            
            # 체력이 0 이하가 되면 캐릭터 사망
            if current_health <= 0:
                return -1
                
        # 공격이 없는 시간인 경우 힐링
        else:
            consecutive_healing += 1  # 연속 힐링 시간 증가
            
            # 기본 힐링
            current_health += x
            
            # 연속 성공 보너스
            if consecutive_healing == t:
                current_health += y
                consecutive_healing = 0  # 연속 힐링 초기화
            
            # 최대 체력 제한
            current_health = min(current_health, max_health)
    
    return current_health

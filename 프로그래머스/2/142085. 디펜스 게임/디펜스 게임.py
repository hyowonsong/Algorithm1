# 디펜스 게임

# 1. 준호가 보유한 병사 n명으로 연속되는 적의 공격을 순서대로 막는 게임
# 2. 매 라운드마다 enemy[i] 마리의 적이 등장합니다.
# 3. 남은 병사 중 enemy[i]명 만큼 소모하여 enemy[i] 마리의 적을 막을 수 있습니다.
# 4. 게임에는 "무적권"이라는 스킬이 있으며 사용하면 병사 소모없이 공격 막을 수 있음
# 5. 무적권은 최대 k번 사용할 수 있습니다. 

# 준호는 무적권을 적절한 시기에 사용하여 최대한 많은 라운드를 진행하고 싶습니다.
# [제한 사항] 1<= n <= 1000000000, 1<=k<500000, 1<=enemy의 길이 <=1000000
# 1<=enemy[i] <= 1000000 

from heapq import *

def solution(n, k, enemy):
    max_heap = []  # Max-Heap을 구현하기 위한 리스트트
    answer = 0  
    
    for i in range(len(enemy)): 
        heappush(max_heap, -enemy[i])  # 현재 라운드의 적의 수를 Max-Heap에 추가 (음수로 저장하여 Max-Heap처럼 동작)
        n -= enemy[i]  # 병사 수에서 현재 라운드의 적 수만큼 소모
        
        # 병사가 부족한 경우 처리
        if n < 0:  
            if k > 0:  # 무적권이 남아있다면
                n += -heappop(max_heap)  # 가장 큰 적의 수를 방어하며 병사 수를 보충 (무적권 사용)
                k -= 1  # 무적권 사용 횟수 감소
            else:
                return answer  # 무적권도 없으면 더 이상 방어 불가하므로 현재까지 방어한 라운드 수 반환
        answer += 1  # 방어한 라운드 수 증가
    
    return answer  
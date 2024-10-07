
import heapq  

def solution(food_times, k):
    # 모든 음식을 다 먹는 시간이 K보다 작거나 같으면 더 먹을 음식이 없으므로 -1 반환
    if sum(food_times) <= k:
        return -1

    # 우선순위 큐(최소 힙)를 사용하여 음식을 먹는 데 걸리는 시간을 기준으로 정렬
    q = []
    for i in range(len(food_times)):
        # (음식을 먹는 데 걸리는 시간, 음식 번호)를 최소 힙에 저장
        heapq.heappush(q, (food_times[i], i + 1))  # 음식 번호는 1부터 시작하므로 i + 1

    total_time = 0  # 총 소비한 시간 
    previous = 0    # 이전 음식에 걸린 시간 
    length = len(food_times)  # 현재 남은 음식 개수

    # 가장 시간이 적게 걸리는 음식부터 처리. 
    # (현재 음식 시간 - 이전 음식 시간) * 남은 음식 개수 만큼의 시간이 소비됨
    while total_time + (q[0][0] - previous) * length <= k:
        # 가장 적은 시간이 걸리는 음식의 시간을 꺼냄
        now = heapq.heappop(q)[0]  # 가장 작은 음식의 먹는 시간 (now)
        
        # 총 시간에 이번에 처리할 음식들을 모두 먹는 시간을 더함
        total_time += (now - previous) * length
        
        # 이번에 먹은 음식이 빠졌으므로 남은 음식 개수를 1 줄임
        length -= 1
        
        # 이전 음식 시간을 현재 음식 시간으로 갱신 (다음 음식을 위해)
        previous = now

    # 남은 음식들을 음식 번호 순서대로 정렬
    result = sorted(q, key=lambda x: x[1])

    # 남은 시간 동안 몇 번째 음식을 먹어야 하는지 계산
    # (K에서 남은 시간을 계산한 뒤 그 순서에 해당하는 음식 번호 반환)
    return result[(k - total_time) % length][1]

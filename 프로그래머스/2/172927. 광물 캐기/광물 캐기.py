def solution(picks, minerals):
    # 피로도 테이블 정의
    fatigue_table = {
        "diamond": [1, 5, 25],
        "iron": [1, 1, 5],
        "stone": [1, 1, 1],
    }
    
    # 사용 가능한 곡괭이의 총 개수
    pick_count = sum(picks)
    
    # 사용 가능한 곡괭이로 캘 수 있는 광물까지만 고려
    minerals = minerals[:pick_count * 5]
    
    # 광물을 5개씩 묶어서 그룹화
    groups = []
    for i in range(0, len(minerals), 5):
        groups.append(minerals[i:i + 5])
        
    # 각 그룹별 피로도 계산
    group_fatigues = []
    for group in groups:
        fatigue = [0, 0, 0]  # diamond, iron, stone 곡괭이로 캤을 때의 피로도
        for mineral in group:
            for i in range(3):
                fatigue[i] += fatigue_table[mineral][i]
        group_fatigues.append(fatigue)
        
    # 피로도가 높은 그룹 우선 순위로 정렬 (돌 곡괭이 기준)
    group_fatigues.sort(key=lambda x: x[2], reverse=True)
    
    # 곡괭이 사용
    total = 0
    for fatigue in group_fatigues:
        if sum(picks) == 0:  # 사용할 곡괭이가 없으면 종료
            break
        for i in range(3):  # diamond, iron, stone 순서로 곡괭이 선택
            if picks[i] > 0:
                total += fatigue[i]
                picks[i] -= 1
                break
    return total
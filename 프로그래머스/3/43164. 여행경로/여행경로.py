def dfs(tickets, route, used):
    # 모든 항공권을 사용했으면 경로 반환
    if len(used) == len(tickets):
        return route
    
    # 현재 위치
    current = route[-1]
    
    # 현재 위치에서 출발하는 모든 항공권을 찾아서 시도
    available_tickets = []
    for i in range(len(tickets)):
        if i not in used and tickets[i][0] == current:
            available_tickets.append((i, tickets[i][1]))
    
    # 알파벳 순으로 정렬
    available_tickets.sort(key=lambda x: x[1])
    
    # 각 항공권으로 이동 시도
    for ticket_idx, next_airport in available_tickets:
        used.add(ticket_idx)
        result = dfs(tickets, route + [next_airport], used)
        if result is not None:
            return result
        used.remove(ticket_idx)
    
    return None

def solution(tickets):
    # ICN에서 시작하는 경로 찾기
    initial_route = ["ICN"]
    used_tickets = set()
    
    return dfs(tickets, initial_route, used_tickets)
def solution(players, callings):
    # 선수 이름 -> 인덱스 맵핑 
    player_index = {}
    for i, name in enumerate(players):
        player_index[name] = i

    
    # 호출된 선수들에 대해 순위를 바꿈
    for called_player in callings:
        idx = player_index[called_player]  # 추월된 선수의 현재 인덱스
        if idx > 0:
            # 추월된 선수가 앞에 있는 선수와 위치를 바꿈
            prev_player = players[idx - 1]
            
            # 위치를 교환
            players[idx - 1], players[idx] = players[idx], players[idx - 1]
            player_index[called_player] -= 1
            player_index[prev_player] += 1
    
    return players

import sys
sys.setrecursionlimit(10000000) 

def solution(k, room_number):
    def find(room):
        # 방 번호의 부모를 찾아 경로 압축
        if room not in parent:
            parent[room] = room + 1  # 다음 방을 초기화
            return room
        parent[room] = find(parent[room])  # 경로 압축
        return parent[room]
    
    parent = {}  # 각 방 번호의 부모를 저장하는 딕셔너리
    result = []
    
    for room in room_number:
        assigned_room = find(room)  # 빈 방 번호를 찾음
        result.append(assigned_room)
    
    return result

# 오픈채팅방 문제 해결 함수
def solution(record):
    user_dict = {}  # 사용자 ID와 최종 닉네임을 저장할 딕셔너리
    actions = []  # 최종 메시지를 저장할 리스트
    
    # 첫 번째 순회: 사용자 ID와 최종 닉네임 매핑
    for r in record:
        parts = r.split(' ')  # 각 레코드를 공백으로 분리
        action = parts[0]  # 첫 번째 요소는 액션(Enter, Leave, Change)
        user_id = parts[1]  # 두 번째 요소는 사용자 ID
        
        # Enter나 Change 액션의 경우 닉네임 업데이트
        if action in ["Enter", "Change"]:
            nickname = parts[2]  # 세 번째 요소는 닉네임
            user_dict[user_id] = nickname  # 사용자 ID와 닉네임 매핑 업데이트
    
    # 두 번째 순회: 최종 메시지 생성
    for r in record:
        parts = r.split(' ')  # 각 레코드를 다시 공백으로 분리
        action = parts[0]  # 액션 확인
        user_id = parts[1]  # 사용자 ID 확인
        
        # Enter 액션: 입장 메시지 생성
        if action == "Enter":
            actions.append(f"{user_dict[user_id]}님이 들어왔습니다.")
        # Leave 액션: 퇴장 메시지 생성
        elif action == "Leave":
            actions.append(f"{user_dict[user_id]}님이 나갔습니다.")
    
    return actions  # 최종 메시지 리스트 반환
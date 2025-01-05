# 오픈채팅방 문제 해결 함수
def solution(record):
    user_dict = {}  # 사용자 ID와 최종 닉네임을 매핑할 딕셔너리
    actions = []  # 최종 메시지를 저장할 리스트
    
    # 첫 번째 순회: 사용자 ID와 최종 닉네임 매핑
    for r in record:
        parts = r.split(' ')  # 각 레코드를 공백으로 분리
        
        # Enter나 Change 액션의 경우 닉네임 업데이트
        if parts[0] in ["Enter", "Change"]:
            nickname = parts[2]  # 세 번째 요소는 닉네임
            # 사용자 ID와 닉네임 매핑 업데이트
            user_dict[parts[1]] = nickname  
    
    # 두 번째 순회: 최종 메시지 생성
    for r in record:
        parts = r.split(' ')  # 각 레코드를 다시 공백으로 분리
        
        # Enter 액션: 입장 메시지 생성
        if parts[0] == "Enter":
            actions.append(f"{user_dict[parts[1]]}님이 들어왔습니다.")
        # Leave 액션: 퇴장 메시지 생성
        elif parts[0] == "Leave":
            actions.append(f"{user_dict[parts[1]]}님이 나갔습니다.")
    
    return actions  # 최종 메시지 리스트 반환
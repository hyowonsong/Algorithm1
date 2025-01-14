def check_distance(place):
    # 응시자들의 위치를 찾습니다
    people = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                people.append((i, j))
    
    # 각 응시자 쌍에 대해 거리두기를 확인합니다
    for i in range(len(people)):
        for j in range(i + 1, len(people)):
            person1 = people[i]
            person2 = people[j]
            
            # 맨해튼 거리 계산
            distance = abs(person1[0] - person2[0]) + abs(person1[1] - person2[1])
            
            # 거리가 1인 경우는 무조건 거리두기 위반
            if distance == 1:
                return 0
                
            # 거리가 2인 경우 파티션 여부 확인
            elif distance == 2:
                # 같은 행에 있는 경우
                if person1[0] == person2[0]:
                    mid_col = (person1[1] + person2[1]) // 2
                    if place[person1[0]][mid_col] != 'X':
                        return 0
                
                # 같은 열에 있는 경우
                elif person1[1] == person2[1]:
                    mid_row = (person1[0] + person2[0]) // 2
                    if place[mid_row][person1[1]] != 'X':
                        return 0
                
                # 대각선에 있는 경우
                else:
                    if not (place[person1[0]][person2[1]] == 'X' and 
                           place[person2[0]][person1[1]] == 'X'):
                        return 0
    
    return 1

def solution(places):
    result = []  # 결과를 담을 리스트
    for place in places:  # 각 대기실 순회
        place_as_list = [list(row) for row in place]  # 문자열 배열을 리스트 배열로 변환
        result.append(check_distance(place_as_list))  # 거리두기 검사 결과 추가
    return result

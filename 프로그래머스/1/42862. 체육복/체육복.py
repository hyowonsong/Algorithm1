def solution(n, lost, reserve):
    # 맨 처음 리스트에 전부 1넣기!
    students = [1] * (n + 1)  
    
    # 도난당한 학생 처리
    for l in lost:
        students[l] -= 1
    
    # 여벌 체육복이 있는 학생 처리
    for r in reserve:
        students[r] += 1
    
    # 체육복 빌려주기
    for i in range(1, n+1):
        # 여기 students[i] == 0 이거 추가해줘야
        if students[i] == 0:
            # 앞번호 학생에게 빌리기(범위 반드시 존재해야)
            if i > 1 and students[i-1] > 1:
                students[i-1] -= 1
                students[i] += 1
                
            # 뒷번호 학생에게 빌리기
            elif i < n and students[i+1] > 1:
                students[i+1] -= 1
                students[i] += 1
                
    
    # 체육복이 있는 학생 수 세기
    count = 0
    for i in range(1, len(students)):
        if students[i] > 0:
            count += 1
    return count
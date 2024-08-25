def solution(n, lost, reserve):
    # 1은 체육복이 있음, 0은 없음을 의미
    students = [1] * (n + 1)  # 0번 인덱스는 사용하지 않음
    
    # 도난당한 학생 처리
    for l in lost:
        students[l] -= 1
    
    # 여벌 체육복이 있는 학생 처리
    for r in reserve:
        students[r] += 1
    
    # 체육복 빌려주기
    for i in range(1, n+1):
        if students[i] == 0:
            # 앞번호 학생에게 빌리기
            if i > 1 and students[i-1] > 1:
                students[i-1] -= 1
                students[i] += 1
                
            # 뒷번호 학생에게 빌리기
            elif i < n and students[i+1] > 1:
                students[i+1] -= 1
                students[i] += 1
                
    
    # 체육복이 있는 학생 수 세기
    count = 0
    for i in range(1, n+1):
        if students[i] > 0:
            count += 1
    
    return count
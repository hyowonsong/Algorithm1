def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 0
        # 작업 리스트의 진도를 증가시킴
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        # 맨 앞의 작업의 진도가 100 이상인 동안 반복
        # while문을 써줘서 이거 계속 될동안 반복
        while progresses and progresses[0] >= 100:      
            cnt += 1
            # 해당 작업과 작업 속도를 리스트에서 제거
            progresses.pop(0)
            speeds.pop(0)

        # 만약 오늘 기능이 배포되었다면 결과 리스트에 추가
        if cnt:
            answer.append(cnt)
    
    return answer

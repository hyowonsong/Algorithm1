def solution(scores):
    rank = 1
    my_score = scores[0]
    scores.sort(key=lambda x: (-x[0], x[1]))
    top_score = scores[0]
    
    for i in range(len(scores)):
        if my_score[0]<top_score[0] and my_score[1]<top_score[1]:
            return -1
                
        if scores[i][1]>=top_score[1]:
            if sum(scores[i])>sum(my_score):
                rank += 1
                
            top_score = scores[i]
        
    return rank
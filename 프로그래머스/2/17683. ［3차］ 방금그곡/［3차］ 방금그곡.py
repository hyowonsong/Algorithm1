# 방금 그곡

def preprocess_melody(melody):
    # 모든 샾(#)이 붙은 음을 단일 문자로 대체합니다
    return melody.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a').replace('B#', 'b')

def get_played_melody(sheet, play_time):
    # 전체 재생된 멜로디를 계산합니다
    full_played_melody = (sheet * (play_time // len(sheet) + 1))[:play_time]
    return full_played_melody

def solution(m, musicinfos):
    m = preprocess_melody(m)
    found = None
    max_play_time = -1
    
    for info in musicinfos:
        start, end, title, sheet = info.split(',')
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        
        play_time = (end_h * 60 + end_m) - (start_h * 60 + start_m)
        sheet = preprocess_melody(sheet)
        played_melody = get_played_melody(sheet, play_time)
        
        if m in played_melody:
            if play_time > max_play_time:
                max_play_time = play_time
                found = title
            elif play_time == max_play_time:
                continue  # 재생 시간이 같으면, 먼저 나온 음악 제목을 그대로 유지합니다
    
    if found:
        return found
    else:
        return "(None)"
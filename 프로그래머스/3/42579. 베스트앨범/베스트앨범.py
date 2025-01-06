
def solution(genres, plays):
    # 1. 장르별 총 재생 횟수 계산
    count = {}
    for genre, play in zip(genres, plays):
        if genre in count:
            count[genre] += play
        else:
            count[genre] = play
    
    # 2. 장르별 노래 (고유 번호, 재생 횟수) 리스트 생성
    genre_songs = {}
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre in genre_songs:
            genre_songs[genre].append((idx, play))
        else:
            genre_songs[genre] = [(idx, play)]
    
    # 3. 각 장르별 노래 정렬 (재생 횟수 내림차순, 같은 재생 횟수에서는 고유 번호 오름차순)
    for genre in genre_songs:
        genre_songs[genre].sort(key=lambda x: (-x[1], x[0]))
    
    # 4. 장르별 총 재생 횟수 내림차순으로 장르 정렬
    sorted_genres = sorted(count.items(), key=lambda x: -x[1])
    
    result = []
    
    # 5. 장르별로 가장 많이 재생된 두 곡을 선택
    for genre, play in sorted_genres:
        top_songs = genre_songs[genre][:2]  # 상위 2개 곡
        for song in top_songs:
            result.extend([song[0]])  # 고유 번호만 결과에 추가
    
    return result

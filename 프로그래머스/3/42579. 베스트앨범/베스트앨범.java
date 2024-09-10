import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Stream;

class Solution {
    public int[] solution(String[] genres, int[] plays){
        // HashMap 에 장르(`String`)을 키로 하고, 그 장르에 속하는 곡들의 정보를 담은
        // ArrayList<int[]> 를 값으로 사용합니다.
        // int[0] : 곡의 인덱스(고유 ID) , int[1] : 곡의 재생 횟수
        HashMap<String, ArrayList<int[]>> genreMap = new HashMap<>();

        HashMap<String, Integer> playMap = new HashMap<>();

        // 장르별 총 재생 횟수와 각 곡의 재생 횟수 저장
        for (int i = 0; i < genres.length; i++) {
            String genre = genres[i];
            int play = plays[i];

            // 해당 장르가 처음 등장하는 경우
            if (!genreMap.containsKey(genre)) {
                // 새로운 장르 추가
                genreMap.put(genre, new ArrayList<>());
                // 총 재생 횟수 초기화
                playMap.put(genre, 0);
            }
            // 장르에 해당 곡 정보 추가 (곡의 인덱스, 재생 횟수)
            genreMap.get(genre).add(new int[]{i, play});
            // 해당 장르의 총 재생 횟수 업데이트
            playMap.put(genre, playMap.get(genre) + play);
        }

        ArrayList<Integer> answer = new ArrayList<>();

        // 총 재생 횟수가 많은 장르순으로 내림차순 정렬
        Stream<Map.Entry<String, Integer>> sortedGenre = playMap.entrySet()
                .stream()
                .sorted((o1, o2) -> Integer.compare(o2.getValue(), o1.getValue()));

        // 각 장르 내에서 노래를 재생 횟수 순으로 정렬해 최대 2곡까지 선택
        sortedGenre.forEach(entry -> {
            Stream<int[]> sortedSongs = genreMap.get(entry.getKey()).stream()
                    // 재생 횟수로 내림차순 정렬
                    .sorted((o1, o2) -> Integer.compare(o2[1], o1[1]))
                    // 스트림에서 제한된 수의 요소만을 반환하는 중간 연산
                    .limit(2);
            // 곡의 인덱스를 answer에 추가
            // forEach()는 스트림의 최종 연산으로,
            // 스트림 내의 각 요소에 대해 특정 작업을 수행하는 반복문과 비슷한 역할
            sortedSongs.forEach(song -> answer.add(song[0]));
        });

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}
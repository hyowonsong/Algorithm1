import java.util.HashMap;
import java.util.HashSet;

public class Solution {

    // 좌표평면을 벗어나는지 체크하는 메소드
    // 매개변수로 이동할 좌표(nx, ny)를 받아서 유효한 범위(0 <= x, y < 11) 내에 있는지 확인함
    private static boolean isValidMove(int nx, int ny) {
        return 0 <= nx && nx < 11 && 0 <= ny && ny < 11;
    }

    // 다음 좌표 결정을 위한 HashMap 생성
    // 각 방향(U, D, L, R)에 대해 이동할 좌표의 변화량을 저장하는 HashMap
    private static final HashMap<Character, int[]> location = new HashMap<>();

    // 각 방향에 대한 좌표 이동 정보를 초기화하는 메서드
    private static void initLocation() {
        // 'U'는 위로 이동하므로 y좌표가 1 증가
        location.put('U', new int[]{0, 1});
        // 'D'는 아래로 이동하므로 y좌표가 1 감소
        location.put('D', new int[]{0, -1});
        // 'L'은 왼쪽으로 이동하므로 x좌표가 1 감소
        location.put('L', new int[]{-1, 0});
        // 'R'은 오른쪽으로 이동하므로 x좌표가 1 증가
        location.put('R', new int[]{1, 0});
    }

    // 주어진 이동 명령어(dirs)에 따라 캐릭터를 이동시키는 메소드
    public int solution(String dirs) {
        // 이동 방향 정보 초기화
        initLocation();

        // 좌표평면의 시작점은 (5, 5)로 설정 (중앙)
        int x = 5, y = 5;

        // 좌표 경로를 저장할 HashSet (중복된 경로를 제거하기 위함)
        HashSet<String> answer = new HashSet<>();

        // 명령어 문자열을 한 글자씩 순회하면서 처리
        for (int i = 0; i < dirs.length(); i++) {
            // 현재 명령어에 해당하는 좌표 변화량(offset)을 가져옴
            int[] offset = location.get(dirs.charAt(i));

            // 이동 후의 새로운 좌표(nx, ny)를 계산
            int nx = x + offset[0];
            int ny = y + offset[1];

            // 유효한 범위의 좌표인지 확인하고, 범위를 벗어나면 무시하고 다음 명령어로 넘어감
            if (!isValidMove(nx, ny))
                continue;

            // A에서 B로 이동한 경로를 저장
            answer.add(x + " " + y + " " + nx + " " + ny);

            // B에서 A로 이동한 경로도 저장 (경로는 방향성이 없으므로 양방향으로 저장)
            answer.add(nx + " " + ny + " " + x + " " + y);

            // 좌표를 이동했으므로 현재 위치를 (nx, ny)로 업데이트
            x = nx;
            y = ny;
        }

        // 총 경로 개수를 반환하되, 양방향이므로 중복된 경로가 두 번씩 저장되어 있어 2로 나눔
        return answer.size() / 2;
    }

}

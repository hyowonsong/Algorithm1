import java.util.ArrayDeque;

public class Solution {
    // 두 팀으로 나누어서 진행하며 상대 팀 진영을 먼저 파괴하면 이기는 게임
    // 각 팀은 상대 팀 진영에 최대한 빨리 도착해야 게임을 유리하게

    // 너비 우선 탐색은 가중치가 없는 그래프에서 최단 경로를 보장합니다.
    // 현재 이 문제는 지나가는 칸의 최솟값을 구해야하기 때문에 너비 우선 탐색 사용

    private static final int[] rx = {0,0,-1,1};
    private static final int[] ry = {-1,1,0,0};

    private static class Node{
        int r,c;

        public Node(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

    public int solution(int[][] maps){
        // 맵의 크기를 저장하는 변수 선언
        int N = maps.length;
        int M = maps[0].length;

        // 최단 거리를 저장할 배열 생성
        int[][] dist = new int[N][M];

        //bfs 탐색을 위한 큐 생성
        ArrayDeque<Node> queue = new ArrayDeque<>();
        // 시작 정점에 대해서 큐에 추가, 최단 거리 저장
        queue.addLast(new Node(0,0));
        dist[0][0] = 1;

        // queue 가 빌 때까지 반복
        while (!queue.isEmpty()) {
            Node now = queue.pollFirst();

            // 현재 위치에서 이동할 수 있는 모든 방향
            for (int i = 0; i < 4; i++) {
                int nr = now.r + rx[i];
                int nc = now.c + ry[i];

                // 맵 밖으로 나가는 경우 예외처리
                if (nr < 0 || nc < 0 || nr >= N || nc >= M)
                    continue;

                // 벽으로 가는 경우 예외처리
                if (maps[nr][nc] == 0)
                    continue;

                // 이동한 위치가 처음 방문하는 경우, queue에 추가하고 거리 갱신
                if (dist[nr][nc] == 0) {
                    queue.addLast(new Node(nr, nc));
                    dist[nr][nc] = dist[now.r][now.c] + 1;
                }
            }
        }

        // 목적지까지 최단 거리 반환, 목적지에 도달하지 못한 경우에는 -1 반환
        if (dist[N - 1][M - 1] == 0) {
            return -1;
        } else {
            return dist[N - 1][M - 1];
        }
    }
}
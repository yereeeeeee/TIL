import java.util.*;

public class programmers_1829_윤예리 {
    public static void main(String[] args) {
    }

    class Pos {
        int x;
        int y;

        public Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int[][] visited;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int num = 1;
    static int r, c;
    static int cnt, max;

    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        r = m; c = n;

        visited = new int[m][n];
        boolean flag = false;
        while (true) {
            if (flag) break;

            flag = true;
            for (int i = 0; i < r; i++) {
                for (int j = 0; j < c; j++) {
                    if (picture[i][j] == num && visited[i][j] != 0) {
                        max = Math.max(max, bfs(picture, i, j));
                        cnt += 1;
                        flag = false;
                    }
                }
            }

            num += 1;
        }

        int[] answer = new int[2];
        answer[0] = cnt;
        answer[1] = max;
        return answer;
    }

    int bfs(int[][] arr, int x, int y) {
        ArrayDeque<Pos> dq = new ArrayDeque<>();
        dq.add(new Pos(x, y));
        int value = 0;

        while (!dq.isEmpty()) {
            Pos here = dq.pollFirst();
            visited[here.x][here.y] = 1;

            for (int i = 0; i < 4; i++) {
                int nx = here.x + dx[i];
                int ny = here.y + dy[i];

                if (0<= nx && nx < r && 0 <= ny && ny < c && arr[nx][ny] == num) {
                    visited[nx][ny] = visited[x][y] + 1;
                    value = Math.max(visited[nx][ny], value);
                    dq.add(new Pos(nx, ny));
                }
            }
        }

        return value;
    }
}

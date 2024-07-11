import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

class Pos {
    int x;
    int y;

    public Pos(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class baekjoon_16236_윤예리 {
    static int n;
    static int[][] arr;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int fx, fy;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[n][n];

        StringTokenizer st;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
                if (arr[i][j] == 9) {
                    fx = i; fy = j;
                }
            }
        }

    }

    static void bfs() {
        boolean[][] visited = new boolean[n][n];
        Deque<Pos> q = new LinkedList<>();
        q.offer(new Pos(fx, fy));
        ArrayList<Integer> cand = new ArrayList<>();

        visited[fx][fy] = true;

        while (!q.isEmpty()) {
            Pos now = q.pollLast();

            for (int i = 0; i < 4; i++) {
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];

                if (0 <= nx && nx < n && 0 <= ny && ny < n && !visited[nx][ny]) {
                    
                }
            }

        }
    }
}

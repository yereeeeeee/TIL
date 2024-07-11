import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Pos {
    int x;
    int y;

    public Pos(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

//class Cand implements Comparable {
//    int[] list;
//
//    public Cand(int[] list) {
//        this.list = list;
//    }
//
//    @Override
//    public int compareTo(int[] o) {
//        return ((o1, o2) -> (o1[0] - o2[0]));
//    }
//}

public class baekjoon_16236_윤예리 {
    static int n;
    static int[][] arr;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int fx, fy;
    static ArrayList<int[]> cand = new ArrayList<>();

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

        bfs();
        Arrays.sort(cand, (o1, o2) -> {
            return o1[0] - o2[0], o1[1];
        });

    }

    static void bfs() {
        int[][] visited = new int[n][n];
        Deque<Pos> q = new LinkedList<>();
        q.offer(new Pos(fx, fy));


        visited[fx][fy] = 1;

        while (!q.isEmpty()) {
            Pos now = q.pollLast();
            int x = now.x;
            int y = now.y;

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (0 <= nx && nx < n && 0 <= ny && ny < n && visited[nx][ny] != 0) {
                    if (arr[x][y] > arr[nx][ny] && arr[nx][ny] != 0) {
                        visited[nx][ny] = visited[x][y] + 1;
                        cand.add(new int[]{visited[nx][ny]-1, nx, ny});
                    }
                    else if (arr[x][y] == arr[nx][ny]) {
                        visited[nx][ny] = visited[x][y] + 1;
                        q.offer(new Pos(nx, ny));
                    }
                    else if (arr[nx][ny] == 0) {
                        visited[nx][ny] = visited[x][y] + 1;
                        q.offer(new Pos(nx, ny));
                    }
                }
            }
        }
    }
}

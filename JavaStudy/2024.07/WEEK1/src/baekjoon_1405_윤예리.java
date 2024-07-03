import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class baekjoon_1405_윤예리 {
    static int n, east, west, south, north;
    int[][] arr = new int[30][30];
    int[][] delta = new int[][]{{0, 1, east}, {0, -1, west} , {1, 0, south}, {-1, 0, north}};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());

        east = Integer.parseInt(st.nextToken());
        west = Integer.parseInt(st.nextToken());
        south = Integer.parseInt(st.nextToken());
        north = Integer.parseInt(st.nextToken());
    }

    static void bfs() {


    }
}

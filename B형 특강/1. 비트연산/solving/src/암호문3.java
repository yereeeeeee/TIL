import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class 암호문3 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        for (int tc=1; tc<=10; tc++) {
            long n = Long.parseLong(br.readLine());

            LinkedList<Integer> lst = new LinkedList<>();

            st = new StringTokenizer(br.readLine());
            for (int i=0; i<n; i++) {
                lst.add(Integer.parseInt(st.nextToken()));
            }

            int m = Integer.parseInt(br.readLine());

            st = new StringTokenizer(br.readLine());
            for (int i=0; i<m; i++) {
                String cmd = st.nextToken();
                if (cmd.equals("I")) {
                    int x = Integer.parseInt(st.nextToken());
                    int y = Integer.parseInt(st.nextToken());
                    for(int i=0, insertIdx = x; i<y; i++, insertIdx++) {
                        lst.add(insertIdx, Integer.parseInt(st.nextToken()));
                    }
                }
            }
        }
    }
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class 수열_편집 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());
        for (int tc=1; tc<=T; tc++){
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int l = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            LinkedList<Integer> arr = new LinkedList<>();
            for (int i=0; i<n; i++) {
                arr.add(Integer.parseInt(st.nextToken()));
            }

            for (int i=0; i<m; i++) {
                st = new StringTokenizer(br.readLine());
                String info = st.nextToken();

                if (info.equals("I")) {
                    int idx = Integer.parseInt(st.nextToken());
                    int num = Integer.parseInt(st.nextToken());
                    arr.add(idx, num);
                }
                else if (info.equals("D")) {
                    int num = Integer.parseInt(st.nextToken());
                    arr.remove(num);
                }
                else if (info.equals("C")) {
                    int idx = Integer.parseInt(st.nextToken());
                    int num = Integer.parseInt(st.nextToken());
                    arr.set(idx, num);
                }
            }

            if (arr.size()>=l) {
                System.out.println("#"+tc+" "+arr.get(l));
            } else {
                System.out.println("#"+tc+" -1");
            }

        }
    }
}

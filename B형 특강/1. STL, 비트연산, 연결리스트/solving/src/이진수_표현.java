import java.util.Scanner;

public class 이진수_표현 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int TC = sc.nextInt();
        for (int t=0; t<TC; t++) {
            int n = sc.nextInt();
            int m = sc.nextInt();

            for (int i=0; i<n; i++) {
                if (m>>1 == 0) {
                    System.out.println("#"+t+" OFF");
                    break;
                }
            }
            System.out.println("#"+t+" ON");

        }
    }
}

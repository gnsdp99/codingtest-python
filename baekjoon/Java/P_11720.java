import java.util.Scanner;

public class P_11720 {
    public static void main(String[] args) {
        // Input
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String sNum = sc.next();
        char[] sNumArr = sNum.toCharArray();
        
        int sum = 0;
        for (int i = 0; i < sNumArr.length; i++) {
            sum += sNumArr[i] - '0';
        }
        System.out.println(sum);
    }
}
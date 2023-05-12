import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.io.InputStreamReader;
import java.io.IOException;

public class P_11659 {
    public static void main(String[] args) throws IOException {
        // Input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
    
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        
        int numArr[] = new int[N+1];
        numArr[0] = 0;
        
        st = new StringTokenizer(br.readLine());
        for (int i=1; i < numArr.length; i++) {
            numArr[i] = numArr[i-1] + Integer.parseInt(st.nextToken());
        }
        
        for (int k=0; k < M; k++) {
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken())-1;
            int j = Integer.parseInt(st.nextToken());
            System.out.println(numArr[j] - numArr[i]);
        }
    }
}
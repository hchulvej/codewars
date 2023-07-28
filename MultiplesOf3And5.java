public class MultiplesOf3And5 {
    public static int solution(int number) {
        if (number <= 0) {
            return 0;
        }
        int res = 0;
        int n = 3;

        while (n < number) {
            if (n % 3 == 0) {
                res += n;
            }
            if (n % 5 == 0) {
                res += n;
            }
            if (n % 3 == 0 && n % 5 == 0) {
                res -= n;
            }
            n++;
        }

        return res;
    }
}

public class StringSplit {
    public static String[] solution(String s) {
        if (s.length() % 2 != 0) {
            s += "_";
        }
        String[] asArray = s.split("");
        String[] res = new String[s.length() / 2];
        int i = 0;
        for (int j = 0; j < s.length() / 2; j++) {
            res[j] = asArray[i] + asArray[i+1];
            i += 2;
        }

        return res;
    }
}

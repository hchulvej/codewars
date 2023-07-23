public class AlternateCapitalization {
    public static String[] capitalize(String s){
        String[] res = new String[2];
        res[0] = "";
        res[1] = "";

        for (int i = 0; i < s.length(); i++) {
            char lc = s.charAt(i);
            char uc = Character.toUpperCase(lc);

            if (i % 2 == 0) {
                res[0] += uc;
                res[1] += lc;
            }
            else {
                res[0] += lc;
                res[1] += uc;
            }
        }

        return res;
    }
}

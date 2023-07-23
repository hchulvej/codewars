public class NeedleHaystack {
    public static String findNeedle(Object[] haystack) {
        String res = "found the needle at position ";

        for (int i = 0; i < haystack.length; i++) {
            if (haystack[i] == "needle") {
                res += i;
                return res;
            }
        }

        return res;
    }
}

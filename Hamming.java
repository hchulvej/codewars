public class Hamming {

    private String leftStrand;
    private String rightStrand;

    public Hamming(String leftStrand, String rightStrand) {
        
        int ll = leftStrand.length();
        int lr = rightStrand.length();

        if (ll == 0 && lr > 0) {
            throw new IllegalArgumentException("left strand must not be empty.");
        }

        if (ll > 0 && lr == 0) {
            throw new IllegalArgumentException("right strand must not be empty.");
        }

        if (ll != lr) {
            throw new IllegalArgumentException("leftStrand and rightStrand must be of equal length.");
        }

        this.leftStrand = leftStrand;
        this.rightStrand = rightStrand;
    }

    public int getHammingDistance() {
        int res = 0;

        for (int i = 0; i < this.leftStrand.length(); i++) {
            if (this.leftStrand.charAt(i) != this.rightStrand.charAt(i)) {
                res++;
            }
        }

        return res;
    }
}
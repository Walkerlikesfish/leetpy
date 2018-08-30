// Tricky, >>> and << has be to carefully picked just for the sake of the problem
public class Solution {
    // you need to treat n as an unsigned value
    public int reverseBits(int n) {
        if (n == 0) return 0;
        int x = 0;
        int cnt = 0;
        while ((n & 1) == 0) {
            n >>>= 1;
            cnt++;
        }
        while (n != 0) {
            x <<= 1;
            x += n & 1;
            n >>>= 1;
            cnt++;
        }
        return x << (32 - cnt);
    }
}

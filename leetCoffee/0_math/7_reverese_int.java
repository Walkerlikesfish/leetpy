class Solution {
    public int reverse(int x) {
        if (x == 0) return 0;
        boolean flag = x > 0  ? true : false;
        x = Math.abs(x);
        int y = 0;
        while (x % 10 == 0) {
            x /= 10;
        }
        while (x > 0) {
            if (y > Integer.MAX_VALUE / 10) return 0;
            y = y * 10 + x % 10;
            x /= 10;
        }
        return flag ? y : -y;
    }
}

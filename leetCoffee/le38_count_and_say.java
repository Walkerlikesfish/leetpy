class Solution {
    /*
    // recursive
    public String countAndSay(int n) {
        if (n == 0) return "";
        if (n == 1) return "1";
        if (n == 2) return "11";

        return f(countAndSay(n-1));
    }

    private String f(String x) {
        String y = "";
        int i = 1, len = x.length();
        char ch = x.charAt(0);
        while (i < len) {
            int j = 1;
            while (i < len && x.charAt(i) == ch) {
                i++;
                j++;
            }
            y += String.valueOf(j) + ch;
            if (i < len) {
                ch = x.charAt(i);
                i++;
            }
        }
        if (x.charAt(len - 2) != x.charAt(len - 1)) {
            y += "1" + x.charAt(len - 1);
        }
        return y;
    }
    */

    // iterative

    public String countAndSay(int n) {
        if (n == 0) return "";
        if (n == 1) return "1";

        String res = "11";
        while (n > 2) {
            res = f(res);
            n--;
        }

        return res;
    }

    private String f(String x) {
        StringBuilder y = new StringBuilder();
        int i = 1, len = x.length();
        char ch = x.charAt(0);
        while (i < len) {
            int j = 1;
            while (i < len && x.charAt(i) == ch) {
                i++;
                j++;
            }
            y.append(j).append(ch);
            if (i < len) {
                ch = x.charAt(i);
                i++;
            }
        }
        if (x.charAt(len - 2) != x.charAt(len - 1)) {
            y.append(1).append(x.charAt(len - 1));
        }
        return y.toString();
    }
}

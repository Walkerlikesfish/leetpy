class Solution {
    public boolean isAnagram(String s, String t) {
        int len = s.length();
        if (len != t.length()) return false;

        int[] arrS = new int[256];
        for (int i = 0; i < len; i++) {
            arrS[s.charAt(i)]++;
        }
        for (int i = 0; i < len; i++) {
            arrS[t.charAt(i)]--;
            if (arrS[t.charAt(i)] < 0) {
                return false;
            }
        }

        return true;
    }
}

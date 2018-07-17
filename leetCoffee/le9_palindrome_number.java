class Solution {
    public boolean isPalindrome(int x) {
        // I ain't gonna convert the number to string
        // TO: O(log_10 n))
        
        if (x < 0) return false;
        if (x < 10) return true;
        if (x % 10 == 0) return false;
        
        int z = 0;

        while (z < x) {
            z = 10 * z + x % 10;
            if (x == z) return true;
            x /= 10;
        }
        if (z != x) return false;
        
        return true;
        
    }
}

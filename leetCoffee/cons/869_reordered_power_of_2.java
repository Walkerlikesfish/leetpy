/*
869 reordered power of 2
Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this in a way such that the resulting number is a power of 2.

Example 4:

Input: 24
Output: false

Example 5:

Input: 46
Output: true

*/

// permutation of a string - https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
// http://www.quickperm.org/

class Solution {
    public boolean reorderedPowerOf2(int N) {
        if (N == 0) return false;
        if (N == 1) return true;

        String s = Integer.toString(N);
        return permute(s, 0, s.length() - 1);
    }

    private boolean permute(String s, int l, int r) {

        boolean flag = false;

        if (l == r) {
            if (s.charAt(0) != '0')
                flag = isPowerOfTwo(Integer.parseInt(s));
        } else {

            for (int i = l; i <= r; i++) {
                s = swap(s, l, i);
                flag = flag || permute(s, l+1, r);
                s = swap(s,l, i);
            }
        }
        return flag;

    }

    /**
     * Swap Characters at position
     * @param a string value
     * @param i position 1
     * @param j position 2
     * @return swapped string
     */
    public String swap(String a, int i, int j)
    {
        char temp;
        char[] charArray = a.toCharArray();
        temp = charArray[i] ;
        charArray[i] = charArray[j];
        charArray[j] = temp;
        return String.valueOf(charArray);
    }

    public boolean isPowerOfTwo(int n)
    {
        if (n == 0)
            return false;

        while (n != 1)
        {
            if (n % 2 != 0)
                return false;
            n = n / 2;
        }
        return true;
    }
}

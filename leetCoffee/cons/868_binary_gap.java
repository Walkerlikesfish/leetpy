// https://codereview.stackexchange.com/questions/159650/find-the-binary-gap-of-a-number-n
/*
Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.

If there aren't two consecutive 1's, return 0.



Example 1:

Input: 22
Output: 2
Explanation:
22 in binary is 0b10110.
In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
The first consecutive pair of 1's have distance 2.
The second consecutive pair of 1's have distance 1.
The answer is the largest of these two distances, which is 2.

 */
class Solution {
    public int binaryGap(int N) {
        int gap = 1;

        boolean found = false;
        boolean found_pair = false;
        for (int i = 0; N > 0; N /= 2) {
            if (N % 2 == 0) {
                i++;
            } else {
                if (i >= gap && found == true) {
                    gap = i;
                    found_pair = true;
                }
                found = true;
                i = 1;
            }

        }
        if (found_pair == true)
            return gap;
        else
            return 0;


    }
}

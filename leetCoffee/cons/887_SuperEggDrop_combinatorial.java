/*
Con 97
You are given K eggs, and you have access to a building with N floors from 1 to N.

Each egg is identical in function, and if an egg breaks, you cannot drop it again.

You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a floor higher than F will break, and any egg dropped at or below floor F will not break.

Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N).

Your goal is to know with certainty what the value of F is.

What is the minimum number of moves that you need to know with certainty what F is, regardless of the initial value of F?

Example 1:

Input: K = 1, N = 2
Output: 2
Explanation:
Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
If it didn't break, then we know with certainty F = 2.
Hence, we needed 2 moves in the worst case to know what F is with certainty.

Example 2:

Input: K = 2, N = 6
Output: 3

Example 3:

Input: K = 3, N = 14
Output: 4

 */


// combinatorial Solution
// Time Complexity: O(KlogN)
 class Solution {
     public int superEggDrop(int K, int N) {
         int cursor, upper = N, lower = 0;
         cursor = (upper + lower) / 2;
         while ((upper - lower )>  1) {
             cursor = lower + (upper - lower) / 2;
             if (combinatorial(K, N, cursor) < N) {
                 lower = cursor;
             } else {
                 upper = cursor;
             }
         }

         return lower + 1;
     }

     // k eggs, n floors, t trials (drops)
     // sum_i_1^N combi(t, i) >= n
     // combi(t, i) = combi(t-1,i) + combi(t-1, i-1)
     // combi(t, 0) = 1;
     // combi(t, i) = combi(t, i-1) * (t-i+1) / i;
     private int combinatorial(int k, int n, int t) {
         int res = 0;
         double cnt = 1;

         for (int i = 1; i <= k; i++) {
             // combi(t, i) = combi(t, i-1) * (t-i+1) / i;
             cnt *= (double) t+1-i;
             cnt /= (double) i;
             res += cnt;

             if (res >= n) {
                 break;
             }
         }
         return res;
     }
 }

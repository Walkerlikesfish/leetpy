/*
https://leetcode.com/contest/weekly-contest-93/problems/advantage-shuffle/

870. Advantage Shuffle

  User Accepted: 476
  User Tried: 701
  Total Accepted: 480
  Total Submissions: 1158
  Difficulty: Medium

Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.



Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]

Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]

 */


// Sol 1: it will exceed time limit
 class Solution {
     public int[] advantageCount(int[] A, int[] B) {
         int max = 0;
         int len = A.length;
         int[] curRep = new int[len];
         System.arraycopy(A, 0, curRep, 0, len);
         permute(A, B, max, curRep, 0, len - 1);
         return curRep;
     }

     private int permute(int[] A, int[] B, int curMax, int[] curRep, int l, int r) {
         if (l == r) {
             int calc = calcAdv(A, B);
             if (calc > curMax) {
                 curMax = calc;
                 System.arraycopy(A, 0, curRep, 0, A.length);

                 System.out.print("<");
                 System.out.println(curMax);
                 System.out.println(Arrays.toString(A));
                 System.out.println(">");
             }
             return curMax;
         } else {
             for (int i = l; i <= r; i++) {
                 swap(A, l, i);
                 int res = permute(A, B, curMax, curRep, l + 1, r);
                 curMax = (res > curMax) ?  res : curMax;
                 swap(A, l, i);
             }
             return curMax;
         }
     }

     private int calcAdv(int[] A, int[] B) {
         int k = 0;
         for (int i = 0; i < A.length; i++) {
             if (A[i] > B[i]) {
                 k++;
             }
         }
         return k;
     }

     private void swap(int[] A, int a, int b) {
         int temp = A[b];
         A[b] = A[a];
         A[a] = temp;
     }
 }

 // Sol 2: iterative permutations
 // http://www.quickperm.org/

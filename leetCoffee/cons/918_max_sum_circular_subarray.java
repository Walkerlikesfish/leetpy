/*
918. Maximum Sum Circular Subarray

    User Accepted: 41
    User Tried: 129
    Total Accepted: 41
    Total Submissions: 161
    Difficulty: Medium

Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)



Example 1:

Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3

Example 2:

Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10

 */
/*
 The subproblem is to find the largest sum of contiguous subarray in a non circular situation
 Essentially, the subproblem can be solved by Kadane's Algorithm
  ==> "Maximum Subarray Problem"
  which is actually DP:
  def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

 ------

 2 Cases for this problem:
 wrapped {5, -3, 5} and unwrapped {-3, -2, -1}.
 For unwrapped case: Kadane's Algorithm is enough.
 For wrapped case, however, we need to see this fact:
 the left out elems in the circular array (The {5, -3} of {5, -3, 5}) is left out
 as they are not contributing to the max sum
 If we can find out the sum of them, we can rule them out in the wrapped case.

 This sum can be obtained by running Kadane's Algorithm on a inverted array of A,
 it is because these elems contributes NEGATIVELY in the original A (but the absolute value < max sum circ subarray),
 in the inverted array of A, they are POSItively largest, which can be found by Kadane's Algorithm.

 Thus in the wrapped case, we get the max sum circ subarray by:
 Actual Negative Contribution Sum = - MaxSumCircSubarray Of INVERTED A
 Wrapped Part Sum = TotalArraySum - (- MaxSumCircSubarray Of INVERTED A)
   = TotalArraySum + MaxSumCircSubarray Of INVERTED A

 Then we compare the max of the two cases and choose the max
 */

 class Solution {
     public int maxSubarraySumCircular(int[] A) {
         int len = A.length;

         int maxPos = maxNonCirc(A);

         int maxNeg = 0;

         for (int i = 0; i < len; i++) {
             maxNeg += A[i];
             A[i] = -A[i];
         }
         maxNeg = maxNeg + maxNonCirc(A);
         if (maxNeg == 0) {
             return maxPos;
         }
         return (maxNeg > maxPos) ? maxNeg : maxPos;
     }

     private int maxNonCirc(int[] A) {
         int len = A.length;
         int maxSoFar = A[0], currMax = A[0];
         int cur0 = 0, cur1 = 0;
         for (int i = 1; i < len; i++) {
             int tmp = A[i];
             if (tmp >= currMax + tmp) {
                 cur0 = i;
                 cur1 = i;
                 currMax = tmp;
             } else {
                 cur1 = i;
                 currMax += tmp;
             }
             maxSoFar = Math.max(maxSoFar, currMax);
         }
         return maxSoFar;
     }
 }

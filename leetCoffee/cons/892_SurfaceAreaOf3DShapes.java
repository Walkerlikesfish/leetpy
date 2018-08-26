/*
 Con99

 On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.



Example 1:

Input: [[2]]
Output: 10

Example 2:

Input: [[1,2],[3,4]]
Output: 34

Example 3:

Input: [[1,0],[0,2]]
Output: 16

Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32

 */
 class Solution {
     public int surfaceArea(int[][] grid) {
         int N = grid.length;
         if (N <= 0) return 0;

         int res = 0, top = 0, bottom = 0;

         for (int i = 0; i < N; i++) {
             for (int j = 0; j < N; j++) {
                 if (grid[i][j] > 0) {
                     top++;
                     bottom++;
                     int v = grid[i][j];
                     res += checkNeighbor(grid, v, i-1, j, N);
                     res += checkNeighbor(grid, v, i, j-1, N);
                     res += checkNeighbor(grid, v, i+1, j, N);
                     res += checkNeighbor(grid, v, i, j+1, N);
                 }

             }
         }
         res += top + bottom;
         return res;
     }

     private int checkNeighbor(int[][] grid, int v, int ii, int jj, int N) {
         if (ii < 0 || ii > N-1 || jj < 0 || jj > N-1) return v;
         return Math.max(0, v - grid[ii][jj]);
     }
 }

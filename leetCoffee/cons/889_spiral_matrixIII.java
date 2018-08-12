/*
https://leetcode.com/contest/weekly-contest-97/problems/spiral-matrix-iii/

On a 2 dimensional grid with R rows and C columns, we start at (r0, c0) facing east.

Here, the north-west corner of the grid is at the first row and column, and the south-east corner of the grid is at the last row and column.

Now, we walk in a clockwise spiral shape to visit every position in this grid.

Whenever we would move outside the boundary of the grid, we continue our walk outside the grid (but may return to the grid boundary later.)

Eventually, we reach all R * C spaces of the grid.

Return a list of coordinates representing the positions of the grid in the order they were visited.

    1 <= R <= 100
    1 <= C <= 100
    0 <= r0 < R
    0 <= c0 < C
*/

class Solution {
    public int[][] spiralMatrixIII(int R, int C, int r0, int c0) {

        int[][] result = new int[R * C][2];
        result[0][0] = r0;
        result[0][1] = c0;
        // end by counting
        int count = 1, curSideLen = 1, tmpSideLen = 0;
        // direction // E, S, W, N - 0, 1, 2, 3
        int cur_r = r0, cur_c = c0, cur_d = 0;
        // change direction side length every two directions traveled
        int change_dir = 0;
        while (count < R * C) {
            switch (cur_d) {
                case 0: // E
                    cur_c++;
                    break;
                case 1: // S
                    cur_r++;
                    break;
                case 2: // W
                    cur_c--;
                    break;
                case 3: // N
                    cur_r--;
                    break;
                default:
                    break;
            }
            tmpSideLen++;

            // perimeter check
            // if inbound, count++
            if (perimeterCheck(cur_r, cur_c, R, C)) {
                result[count][0] = cur_r;
                result[count][1] = cur_c;
                count++;
            }

            if (tmpSideLen == curSideLen) {
                // direction change
                tmpSideLen = 0;
                cur_d = (cur_d + 1) % 4;
                change_dir++;
            }
            if (change_dir == 2) {
                // side length change
                curSideLen++;
                change_dir = 0;
            }
        }
        return result;
    }

    boolean perimeterCheck(int r, int c, int R, int C) {
        if (r < R && c < C && r >= 0 && c >= 0) {
            return true;
        }
        return false;
    }
}

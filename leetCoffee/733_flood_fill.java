class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        if (image == null) return null;
        int rows = image.length, cols = image[0].length;
        int curColor = image[sr][sc];
        if (curColor == newColor) return image;
        int[][] img = image;
        Queue<Coor> queue = new LinkedList<>();
        List<Coor> dirs = new ArrayList<>();
        dirs.add(new Coor(0,1));
        dirs.add(new Coor(0,-1));
        dirs.add(new Coor(1,0));
        dirs.add(new Coor(-1,0));
        queue.offer(new Coor(sr, sc));
        while (queue.size() != 0) {
            // deplete current queue
            int len = queue.size();
            for (int i = 0; i < len; i++) {
                Coor cur = queue.poll();
                img[cur.r][cur.c] = newColor;
                // check four sides
                for (Coor coor : dirs) {
                    int r = coor.r + cur.r;
                    int c = coor.c + cur.c;
                    if (r < 0 || r >= rows || c < 0 || c >= cols || curColor != img[r][c]) {
                        continue;
                    } else {
                        queue.offer(new Coor(r, c));
                    }
                }
            }
        }
        return img;
    }

    class Coor {
        int r;
        int c;
        Coor(int x, int y) {
            r = x;
            c = y;
        }
    }
}

/*
 DFS Recursive
 */
/*
 class Solution {
     public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
         int len = image.length;
         int wid = image[0].length;
         int oldColor = image[sr][sc];
         int[][] marker = new int[len][wid];
         paint(image[sr][sc], newColor, image, sr, sc, marker);
         return image;
     }

     public void paint(int oldColor, int newColor, int[][] image, int cr, int cc, int[][] marker) {
         // left, right, up, down
         if (cr < 0 || cr >= image.length)  return;
         if (cc < 0 || cc >= image[0].length)  return;

         if (marker[cr][cc] != 1 && image[cr][cc] == oldColor) {
             image[cr][cc] = newColor;
             marker[cr][cc] = 1;
             paint(oldColor, newColor, image, cr - 1, cc, marker);
             paint(oldColor, newColor, image, cr + 1, cc, marker);
             paint(oldColor, newColor, image, cr, cc - 1, marker);
             paint(oldColor, newColor, image, cr, cc + 1, marker);
         }
         return;
     }
 }
*/

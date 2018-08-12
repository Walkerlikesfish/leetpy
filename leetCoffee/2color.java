class Solution {
    public boolean possibleBipartition(int N, int[][] dislikes) {
        // 2 color
        // the original 2 color algo only works for connected graph
        // if dislike exists for a, b, then a and b is not neighbor
        Map<Integer, Set<Integer>> map = new HashMap<>();
        for (int i = 0; i < dislikes.length; i++) {
            if (map.containsKey(dislikes[i][0]-1)) {
                map.get(dislikes[i][0]-1).add(dislikes[i][1]-1);
            } else {
                Set<Integer> newSet = new HashSet<>();
                newSet.add(dislikes[i][1]-1);
                map.put(dislikes[i][0]-1, newSet);
            }
        }
        // default int arr elem: 0
        int[][] graph = new int[N][N];
        int[] color = new int[N];
        color[0] = 1; // color 1, 2
    for (int i = 0; i < N; i++) {
            Set<Integer> iset = null;
            if (map.containsKey(i)) {
                iset = map.get(i);
                for (int j = 0; j < N; j++) {
                    if (graph[i][j] == -1) {
                        continue;
                    }
                    if (iset.contains(j)) {
                        graph[i][j] = -1;
                        graph[j][i] = -1;
                    } else {
                        graph[i][j] = 1;
                    }
                }
            } else {
                for (int j = 0; j < N; j++) {
                    if (graph[i][j] == 0)
                    {
                        graph[i][j] = 1; // connected
                    }
                }
            }
            graph[i][i] = -1;
        }
        for (int i = 0; i < N; i++){
            System.out.println(Arrays.toString(graph[i]));
        }



        // coloring
        LinkedList<Integer>q = new LinkedList<Integer>();
        // start from the first person
        q.add(0);

        // BFS
        while (q.size() != 0)
        {
            int u = q.poll();
            // ignore self loop

            for (int v = 0; v < N; v++)
            {
                // if v not colored yet
                if (graph[u][v] == 1 && color[v] == 0) {
                    color[v] = 3 - color[u];
                    q.add(v);
                } else if (graph[u][v] == 1 && color[v] == color[u]) {
                    return false;
                }
            }
        }
        return true;

    }
}

/*
890. Possible Bipartition

Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group.

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.



Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]

Note:

    1 <= N <= 2000
    0 <= dislikes.length <= 10000
    1 <= dislikes[i][j] <= N
    dislikes[i][0] < dislikes[i][1]
    There does not exist i != j for which dislikes[i] == dislikes[j].

*/

class Solution {
    public boolean possibleBipartition(int N, int[][] dislikes) {
        // 2 color
        // the original 2 color algo only works for connected graph
        // if dislike exists for a, b, then a and b is neighbor

        // the requirement for a disconnected graph to be bipartite:
        //    every connected component is bipartite
        // --> we only need to care about the people with dislikes
        // we can ignore people likes and liked by every other person

        if (N == 1) return true;

        Set<Integer> inDislike = new HashSet<>();
        Map<Integer, Set<Integer>> map = new HashMap<>();
        for (int i = 0; i < dislikes.length; i++) {
            inDislike.add(dislikes[i][0]);
            inDislike.add(dislikes[i][1]);
            if (map.containsKey(dislikes[i][0]-1)) {
                map.get(dislikes[i][0]-1).add(dislikes[i][1]-1);
            } else {
                Set<Integer> newSet = new HashSet<>();
                newSet.add(dislikes[i][1]-1);
                map.put(dislikes[i][0]-1, newSet);
            }
        }
        int k = inDislike.size();
        // default int arr elem: 0
        int[][] graph = new int[k][k];
        int[] color = new int[k];
        color[0] = 1; // color 1, 2
        for (int i = 0; i < k; i++) {
            Set<Integer> iset = null;
            if (map.containsKey(i)) {
                iset = map.get(i);
                for (int j = 0; j < k; j++) {
                    if (graph[i][j] == 1) {
                        // connected if dislike
                        continue;
                    }
                    if (iset.contains(j)) {
                        graph[i][j] = 1;
                        graph[j][i] = 1;
                    } else {
                        graph[i][j] = -1;
                    }
                }
            } else {
                for (int j = 0; j < k; j++) {
                    if (graph[i][j] == 0)
                    {
                        graph[i][j] = -1; // disconnected
                    }
                }
            }
            graph[i][i] = -1;
        }

        // if the graph is not connected,

        // if the graph is connected, we can check by coloring
        // coloring
        LinkedList<Integer>q = new LinkedList<Integer>();
        // start from the first person
        q.add(0);

        // BFS
        while (q.size() != 0)
        {
            int u = q.poll();
            // ignore self loop

            for (int v = 0; v < k; v++)
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

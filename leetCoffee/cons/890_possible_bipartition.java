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
        // not a 2 color problem
        int[] partition = new int[N]; // each person: group0 or group 1
        Map<Integer, Set<Integer>> map = new HashMap<>();
        for (int i = 0; i < dislikes.length; i++) {
            if (map.containsKey(dislikes[i][0]-1)) {
                map.get(dislikes[i][0]-1).add(dislikes[i][1]-1);
            } else {
                Set<Integer> newSet = new HashSet<>();
                newSet.add(dislikes[i][1]-1);
                map.put(dislikes[i][0]-1, newSet);
            }
            if (map.containsKey(dislikes[i][1]-1)) {
                map.get(dislikes[i][1]-1).add(dislikes[i][0]-1);
            } else {
                Set<Integer> newSet = new HashSet<>();
                newSet.add(dislikes[i][0]-1);
                map.put(dislikes[i][1]-1, newSet);
            }
        }
        // System.out.println(map.toString());
        // N queens, 2 * N board

        // return traverse(N, partition, 0, map);
        return traverse2(N, partition, map);
    }

    public boolean ifConflict(int[] partition, int k, Map<Integer, Set<Integer>> map) {
        for (int i = 0; i < k; i++) {
            if (partition[i] == partition[k]) {
                if (map.containsKey(i) && map.get(i).contains(k)) {
                    return true; // conflict
                }
            }
        }
        return false;
    }

    // recursive
    // exceeding time limit
    public boolean traverse(int N, int[] partition, int k, Map<Integer, Set<Integer>> map) {
        if (k >= N) {
            return true;
        } else {
            partition[k] = 0;
            if (!ifConflict(partition, k, map)) {
                if (traverse(N, partition, k+1, map)) {
                    return true;
                }
            }
            partition[k] = 1;
            if (!ifConflict(partition, k, map)) {
                if (traverse(N, partition, k+1, map)) {
                    return true;
                }
            }
        }
        return false;
    }

    // iterative
    // exceeding time limit
    public boolean traverse2(int N, int[] partition, Map<Integer, Set<Integer>> map) {
        int k = 0;
        while (k >= 0) {
            while (partition[k] < 2) {
                partition[k] += 1;
                if (k == N-1 && !ifConflict(partition, k, map)) {
                    return true;
                } else {
                    if (!ifConflict(partition, k, map)) {
                        k++;
                    }
                }
            }
            partition[k] = 0;
            k--;
        }
        return false;
    }
}

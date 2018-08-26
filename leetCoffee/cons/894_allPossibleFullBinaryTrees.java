/*
con 99

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.



Example 1:

Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]

 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<TreeNode> allPossibleFBT(int N) {
         /*
            N == 3 is the basic form that have only 1 possible topo

            Traverse all combinations in this fashion:
                1, 1, n-2
                3, 1, n-4
                ...
                n-2, 1, 1
            Of course we can use a recursive method
            But I don't want to
        */

        Map<Integer, List<TreeNode>> topos = new HashMap<>();
        TreeNode root = new TreeNode(0);
        List<TreeNode> baseFbt = new ArrayList<>();
        if (N % 2 == 0) return baseFbt;

        baseFbt.add(root);
        topos.put(1, baseFbt);
        for (int i = 3; i <= N; i += 2) {
            List<TreeNode> fbt = new ArrayList<>();

            for (int j = 1; j <= i-2; j += 2) {
                List<TreeNode> left = topos.get(j);
                List<TreeNode> right = topos.get(i - 1 - j);
                for (int m = 0; m < left.size(); m++) {
                    for (int n = 0; n < right.size(); n++) {
                        root = new TreeNode(0);
                        root.left = left.get(m);
                        root.right = right.get(n);
                        fbt.add(root);
                    }
                }
            }
            topos.put(i, fbt);
        }
        return topos.get(N);
    }

}

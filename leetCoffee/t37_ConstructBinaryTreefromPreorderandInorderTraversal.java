/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */

/*
    We suppose that there are no duplicates in the tree
 */

public class Solution {
    /**
     * @param inorder: A list of integers that inorder traversal of a tree
     * @param postorder: A list of integers that postorder traversal of a tree
     * @return: Root of a tree
     */
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder == null || inorder == null || preorder.length == 0 || inorder.length == 0)
            return null;
        
        // <value, idx>
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            map.put(inorder[i], i);
        }
        
        return buildT(preorder, map, 0, preorder.length, 0);
    }
    
    // num: num of nodes in total considered for this root
    // offset: offset where the child tree starts
    public TreeNode buildT(int[] preorder, Map<Integer, Integer> map, int beg, int num, int offset) {
        if (num == 0) return null;
        TreeNode root = new TreeNode(preorder[beg]);
        // size of left child tree
        int i = map.get(root.val) - offset;
        root.left = buildT(preorder, map, beg + 1, i , offset);
        root.right = buildT(preorder, map,beg + i + 1, num - (i + 1), offset + i + 1);
        return root;
    }
}

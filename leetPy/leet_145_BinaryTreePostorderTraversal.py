class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        st = [root]
        cur_ptr = root
        while st:
            cur_ptr = st[-1]
            if cur_ptr.left:
                st.append(cur_ptr.left)
                cur_ptr.left = None
            elif cur_ptr.right:
                st.append(cur_ptr.right)
                cur_ptr.right = None
            else:
                pop_ptr = st.pop()
                res.append(pop_ptr.val)
        return res
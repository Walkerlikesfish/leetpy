class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        st = [root]
        res = []
        while st:
            head_ptr = st.pop()
            res.append(head_ptr.val)
            if head_ptr.right:
                st.append(head_ptr.right)
            if head_ptr.left:
                st.append(head_ptr.left)
        return res
# Definition for a binary tree node.
import json

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if pre:
            root = TreeNode(pre[0])
            if len(pre) > 1:
                l = pre[1]
                r = post[-2]
                if l == r:
                    root.left = self.constructFromPrePost(pre[1:], post[:-1])
                else:
                    post_l_ind = post.index(l)
                    pre_r_ind = pre.index(r)
                    root.left = self.constructFromPrePost(pre[1:pre_r_ind], post[:post_l_ind+1])
                    root.right = self.constructFromPrePost(pre[pre_r_ind:], post[post_l_ind+1:-1])
            return root
        else:
            return None


def stringToIntegerList(input):
    return json.loads(input)


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


def main():
    import sys

    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            pre = stringToIntegerList(line)
            line = sys.stdin.readline().rstrip('\n')
            post = stringToIntegerList(line)

            ret = Solution().constructFromPrePost(pre, post)

            out = treeNodeToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
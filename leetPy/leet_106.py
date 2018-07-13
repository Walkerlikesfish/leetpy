# Definition for a binary tree node.
import json
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(postorder) == 0:
            return None
        else:
            croot = postorder[-1]
            cind = inorder.index(croot)
            cnode = TreeNode(croot)
            cnode.left = self.buildTree(inorder[0:cind], postorder[0:cind])
            cnode.right = self.buildTree(inorder[cind+1:], postorder[cind:-1])
            return cnode


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
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            inorder = stringToIntegerList(line)
            line = sys.stdin.readline().rstrip('\n')
            postorder = stringToIntegerList(line)

            ret = Solution().buildTree(inorder, postorder)

            out = treeNodeToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
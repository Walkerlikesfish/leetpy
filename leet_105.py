# Definition for a binary tree node.
import json
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        else:
            root = TreeNode(preorder[0])
            ids = inorder.index(preorder[0])
            root.left = self.buildTree(preorder[1:ids+1],inorder[:ids])
            root.right = self.buildTree(preorder[ids+1:],inorder[ids+1:])
            return root

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
            preorder = stringToIntegerList(line)
            line = sys.stdin.readline().rstrip('\n')
            inorder = stringToIntegerList(line)

            ret = Solution().buildTree(preorder, inorder)

            out = treeNodeToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
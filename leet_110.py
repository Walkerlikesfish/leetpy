# Definition for a binary tree node.
import json

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        self.isB = True
        self.calcDepth(root)
        return self.isB

    def calcDepth(self,root):
        if self.isB:
            if root is None:
                return 0
            else:
                ldepth = self.calcDepth(root.left)
                rdepth = self.calcDepth(root.right)
                if abs(ldepth - rdepth) > 1:
                    self.isB = False

                return max(ldepth, rdepth) + 1
        else:
            return 0


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            root = stringToTreeNode(line)

            ret = Solution().isBalanced(root)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
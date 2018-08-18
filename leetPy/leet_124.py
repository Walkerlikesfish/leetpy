# Definition for a binary tree node.
import json

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = -99999999999999
        self.findLongestPath(root)
        return self.res

    def findLongestPath(self, root):
        if root is None:
            return 0
        else:
            lp = self.findLongestPath(root.left)
            rp = self.findLongestPath(root.right)
            if lp + rp + root.val > self.res:
                self.res = lp + rp + root.val
            print self.res, lp, rp, root.val
            return max(root.val + max(lp, rp), 0)


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


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys

    while True:
        try:
            line = sys.stdin.readline().strip('\n')
            root = stringToTreeNode(line)

            ret = Solution().maxPathSum(root)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
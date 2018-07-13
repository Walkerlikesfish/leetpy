# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import json

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.genBST(1, n)

    def genBST(self, left, right):
        # [left, right]
        if left > right:
            return [None]
        elif left == right:
            return [TreeNode(left)]
        else:
            resRoot = []
            for i in range(left, right+1):
                leftRoots = self.genBST(left, i-1)
                rightRoots = self.genBST(i+1, right)
                for lroot in leftRoots:
                    for rroot in rightRoots:
                        curRoot = TreeNode(i)
                        curRoot.left = lroot
                        curRoot.right = rroot
                        resRoot.append(curRoot)
            return resRoot


def stringToInt(input):
    return int(input)


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


def treeNodeArrayToString(treeNodeArray):
    serializedTreeNodes = []
    for treeNode in treeNodeArray:
        serializedTreeNode = treeNodeToString(treeNode)
        serializedTreeNodes.append(serializedTreeNode)
    return "[{}]".format(', '.join(serializedTreeNodes))


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            n = stringToInt(line)

            ret = Solution().generateTrees(n)

            out = treeNodeArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
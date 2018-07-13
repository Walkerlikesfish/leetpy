# Definition for a binary tree node.
import json

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return 0
        curs = [root.val]
        nxts = []
        sq = [root]
        nxt = []
        finished = False
        while not finished:
            finished = True
            for qi, eq in enumerate(sq):
                if eq is not None:
                    finished = False
                    cr = curs[qi]
                    if eq.left is not None:
                        nxts.append(cr+eq.left.val)
                    else:
                        nxts.append(cr)
                    if eq.right is not None:
                        nxts.append(cr+eq.right.val)
                    else:
                        nxts.append(cr)
                    nxt.append(eq.left)
                    nxt.append(eq.right)
                else:
                    continue
            sq = nxt
            nxt = []
        return cnt




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


def int2dArrayToString(input):
    return json.dumps(input)


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

            ret = Solution().levelOrder(root)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
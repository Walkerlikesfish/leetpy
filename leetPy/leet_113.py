# Definition for a binary tree node.
import json

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.rs = sum
        self.res = []
        self.searchTreeDeep(root, [], 0)
        return self.res

    def searchTreeDeep(self, cur_root, q, s):
        if cur_root is None:
            return
        else:
            newq = list(q)
            newq.append(cur_root.val)
            news = s+cur_root.val
            if cur_root.left is None and cur_root.right is None: # cur node is a leaf node
                if news == self.rs:
                    self.res.append(newq)
                else:
                    return
            else:
                if cur_root.left is not None:
                    self.searchTreeDeep(cur_root.left, newq, news)
                if cur_root.right is not None:
                    self.searchTreeDeep(cur_root.right, newq, news)


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


def stringToInt(input):
    return int(input)


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
            line = sys.stdin.readline().rstrip('\n')
            sum = stringToInt(line)

            ret = Solution().pathSum(root, sum)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
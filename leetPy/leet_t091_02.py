# Definition for a binary tree node.
import json
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.pa = None
        self.visited = False

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        if root is None:
            return []
        res = []
        sq = [root]
        sqp = [None]
        nxt = []
        nxtp = []
        finished = False

        target = int(target.val)
        K = int(K)

        while not finished:
            finished = True
            for ieq,eq in enumerate(sq):
                if eq is not None:
                    if eq.val == target:
                        tar_root = eq
                    eq.pa = sqp[ieq]
                    finished = False
                    nxt.append(eq.left)
                    nxtp.append(eq)
                    nxt.append(eq.right)
                    nxtp.append(eq)
                else:
                    continue
            sq = nxt
            sqp = nxtp
            nxt = []
            nxtp = []

        # search from tar_root
        cnt_lv = 0
        sq = [tar_root]
        nxt = []
        while cnt_lv < K:
            cnt_lv += 1
            for eq in sq:
                eq.visited = True
                if eq.left is not None and not eq.left.visited:
                    nxt.append(eq.left)
                if eq.right is not None and not eq.right.visited:
                    nxt.append(eq.right)
                if eq.pa is not None and not eq.pa.visited:
                    nxt.append(eq.pa)
            sq = nxt
            nxt = []

        res = []
        for eq in sq:
            res.append(eq.val)

        return res


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

    while True:
        try:
            line = sys.stdin.readline().strip('\n')
            root = stringToTreeNode(line)

            target = sys.stdin.readline().strip('\n')
            K = sys.stdin.readline().strip('\n')
            ret = Solution().distanceK(root, target, K)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
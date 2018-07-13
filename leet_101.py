# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # use a stack to record the nodes in BFS order
        if root == None:
            return True
        finished = False
        nxt = []
        cur = [root]
        while not finished:
            finished = True
            for el in cur:
                if el is not None:
                    nxt.append(el.left)
                    nxt.append(el.right)
            n = len(nxt)
            for i in range(n/2):
                if nxt[i] is None:
                    l = -1
                else:
                    l = nxt[i].val
                    finished = False
                if nxt[-i-1] is None:
                    r = -1
                else:
                    r = nxt[-i-1].val
                    finished = False
                if l!=r:
                    return False

            # go iterate
            cur = nxt
            nxt = []
        return True



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

            ret = Solution().isSymmetric(root)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
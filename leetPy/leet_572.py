# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if self.isSame(s, t):
            return True
        elif s:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right,t)
        else:
            return False

    def isSame(self, s, t):
        if s and t:
            if s.val == t.val:
                return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)
            else:
                return False
        else:
            if (not s) and (not t):
                return True
            else:
                return False


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

    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            s = stringToTreeNode(line)
            line = sys.stdin.readline().rstrip('\n')
            t = stringToTreeNode(line)

            ret = Solution().isSubtree(s, t)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
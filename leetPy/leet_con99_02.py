# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if not N:
            return []
        elif N == 1:
            return [TreeNode(0)]
        elif N % 2 == 0:
            return []

        nodes_list = [None] * (N+1)
        nodes_list[1] = [TreeNode(0)]
        for i in range(3, N+1, 2):
            cur_n = i-1
            for j in range(1, cur_n, 2):
                oj = cur_n - j
                for lnode in nodes_list[j]:
                    for rnode in nodes_list[oj]:
                        cur_root = TreeNode(0)
                        cur_root.left = lnode
                        cur_root.right = rnode
                        if not nodes_list[i]:
                            nodes_list[i] = [cur_root]
                        else:
                            nodes_list[i].append(cur_root)
        return nodes_list[N]


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

    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            N = stringToInt(line)

            ret = Solution().allPossibleFBT(N)

            out = treeNodeArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
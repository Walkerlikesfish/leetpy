# Definition for a binary tree node.
import json

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return []

        cnt_lv = 0
        sq = [root]
        nxt = []
        papa_nodes = {}
        res = []

        while sq:
            cnt_lv += 1
            for each_node in sq:
                if each_node.left:
                    papa_nodes[each_node.left] = each_node
                    nxt.append(each_node.left)
                if each_node.right:
                    papa_nodes[each_node.right] = each_node
                    nxt.append(each_node.right)
            if not nxt:
                break
            sq = nxt
            nxt = []

        if len(sq) == 1:
            return sq[0]
        nxt = []
        while sq:
            for each_node in sq:
                res.append(each_node.val)
                if each_node in papa_nodes and papa_nodes[each_node] not in nxt:
                    nxt.append(papa_nodes[each_node])
            if len(nxt) == 1:
                break
            sq = nxt
            nxt = []

        return nxt[0]
        # return res[::-1]


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

    while True:
        try:
            line = sys.stdin.readline().strip('\n')
            root = stringToTreeNode(line)

            ret = Solution().subtreeWithAllDeepest(root)

            out = treeNodeToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
# Definition for a binary tree node.
import json

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def findMax(root):
            cur_ptr = root
            while cur_ptr.right:
                cur_ptr = cur_ptr.right
            return cur_ptr.val

        # find the key first
        if not root:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                root.val = findMax(root.left)
                root.left = self.deleteNode(root.left, root.val)
                return root


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
            line = sys.stdin.readline().rstrip('\n')
            root = stringToTreeNode(line)
            line = sys.stdin.readline().rstrip('\n')
            key = stringToInt(line)

            ret = Solution().deleteNode(root, key)

            out = treeNodeToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
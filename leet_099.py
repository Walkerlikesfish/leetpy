# Definition for a binary tree node.
import json

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # self.p1 = None
        # self.p2 = None
        # self.prev = None
        # self.traverseInOrder(root)
        # self.p2.val, self.p1.val = self.p1.val, self.p2.val

        # Morris InOrderTraverse
        p1 = None
        p2 = None
        prev = None
        cur_ptr = root

        while cur_ptr is not None:
            if cur_ptr.left is None:
                # hit leaf node
                if prev is not None and prev.val > cur_ptr.val:
                    if p1 is None:
                        p1 = prev
                        p2 = cur_ptr
                    else:
                        p2 = cur_ptr
                prev = cur_ptr

                cur_ptr = cur_ptr.right
            else:
                prec_ptr = cur_ptr.left
                # find the precedent of cur_ptr
                # go the right-most nodes of left-sub-tree(cur_ptr)
                while prec_ptr.right is not None and prec_ptr.right is not cur_ptr:
                    prec_ptr = prec_ptr.right

                if prec_ptr.right is None: # find the precedent of cur_ptr
                    prec_ptr.right = cur_ptr
                    cur_ptr = cur_ptr.left
                else:
                    prec_ptr.right = None # the precedent has been visited -> recover the precedent

                    if prev is not None and prev.val > cur_ptr.val:
                        if p1 is None:
                            p1 = prev
                            p2 = cur_ptr
                        else:
                            p2 = cur_ptr
                    prev = cur_ptr

                    cur_ptr = cur_ptr.right
        p2.val, p1.val = p1.val, p2.val

    def traverseInOrder(self, root):
        if root is None:
            return
        else:
            if root.left is not None:  # recursively check the left sub-tree
                self.traverseInOrder(root.left)

            if self.prev is not None and root.val < self.prev.val:
                if self.p1 is None:
                    self.p1 = self.prev
                    self.p2 = root
                else:
                    self.p2 = root

            self.prev = root

            if root.right is not None: # recursively check the right sub-tree
                self.traverseInOrder(root.right)


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
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            root = stringToTreeNode(line)

            ret = Solution().recoverTree(root)

            out = treeNodeToString(root)
            if ret is not None:
                print "Do not return anything, modify root in-place instead."
            else:
                print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
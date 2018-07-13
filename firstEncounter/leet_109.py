# Definition for singly-linked list.
import json

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        cur_node = head
        cnt_list = 0
        while cur_node is not None:
            cur_node = cur_node.next
            cnt_list += 1
        nlist = cnt_list
        if nlist == 1:
            return []
        return self.getRoot(nlist, head)

    def getRoot(self,n,head):
        if n == 0:
            return None
        if n == 1:
            return TreeNode(head.val)
        else:
            cur_node = head
            cur_i = 0
            while cur_node is not None:
                cur_i += 1
                if cur_i == (n+1)/2:
                    break
                else:
                    cur_node = cur_node.next

            root = TreeNode(cur_node.val)
            if cur_i == 1:
                root.left = None
            else:
                root.left = self.getRoot(cur_i-1, head)
            root.right = self.getRoot(n-cur_i, cur_node.next)

            return root




def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


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
            head = stringToListNode(line)

            ret = Solution().sortedListToBST(head)

            out = treeNodeToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
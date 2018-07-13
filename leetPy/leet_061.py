# Definition for singly-linked list.
import json

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        node_ind = []
        n_node = 0
        ptr_cur = head
        while ptr_cur is not None:
            n_node += 1
            node_ind.append(ptr_cur)
            ptr_cur = ptr_cur.next
        k = k%n_node
        if n_node == 0:
            return head
        if k == 0:
            return head
        node_ind[n_node-k-1].next = None
        node_ind[n_node-1].next = head
        head = node_ind[n_node-k]
        return head


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


def stringToInt(input):
    return int(input)


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


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
            line = sys.stdin.readline().rstrip('\n')
            k = stringToInt(line)

            ret = Solution().rotateRight(head, k)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
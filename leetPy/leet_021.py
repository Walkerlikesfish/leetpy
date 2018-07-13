# Definition for singly-linked list.
import json


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        resultRoot = ListNode(0)
        ptr_r = resultRoot
        ptr1 = l1
        ptr2 = l2

        while ptr1 is not None and ptr2 is not None:
            if ptr1.val < ptr2.val:
                ptr_r.next = ListNode(ptr1.val)
                ptr1 = ptr1.next
            else:
                ptr_r.next = ListNode(ptr2.val)
                ptr2 = ptr2.next
            ptr_r = ptr_r.next

        if ptr2 is not None:
            ptr_r.next = ptr2
        if ptr1 is not None:
            ptr_r.next = ptr1
        return resultRoot.next


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
            l1 = stringToListNode(line)
            line = sys.stdin.readline().rstrip('\n')
            l2 = stringToListNode(line)

            ret = Solution().mergeTwoLists(l1, l2)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
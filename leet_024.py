# Definition for singly-linked list.
import json

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        headhead = ListNode(0)
        swap_node = ListNode(0)
        headhead.next = head

        cur_ptr = head
        pre_ptr = headhead

        while pre_ptr.next is not None:
            cur_ptr = pre_ptr.next

            if cur_ptr.next is None:
                break

            swap_node.next = cur_ptr.next.next
            pre_ptr.next = cur_ptr.next
            cur_ptr.next.next = cur_ptr
            cur_ptr.next = swap_node.next

            pre_ptr = pre_ptr.next.next

        return headhead.next


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
            head = stringToListNode(line)

            ret = Solution().swapPairs(head)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
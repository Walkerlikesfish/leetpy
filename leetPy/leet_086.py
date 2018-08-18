# Definition for singly-linked list.
import json

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        head_left = ListNode(0)
        head_right = ListNode(0)
        cur_ptr = head
        ptr_left = head_left
        ptr_right = head_right
        while cur_ptr is not None:
            cur_v = cur_ptr.val
            if cur_v < x:
                ptr_left.next = ListNode(cur_v)
                ptr_left = ptr_left.next
            elif cur_v >= x:
                ptr_right.next = ListNode(cur_v)
                ptr_right = ptr_right.next
            cur_ptr = cur_ptr.next
        ptr_left.next = head_right.next
        return head_left.next



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

    while True:
        try:
            line = sys.stdin.readline().strip('\n')
            head = stringToListNode(line)
            line = sys.stdin.readline().strip('\n')
            x = stringToInt(line)

            ret = Solution().partition(head, x)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
# Definition for singly-linked list.
import json

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        cur_ptr = head.next
        last_pre = head
        while cur_ptr:
            cur_val = cur_ptr.val
            cmp_ptr = head
            pre_ptr = None
            while cmp_ptr.val < cur_val:
                pre_ptr = cmp_ptr
                cmp_ptr = cmp_ptr.next
            if pre_ptr and pre_ptr.next is not cur_ptr:
                last_pre.next = cur_ptr.next
                cur_ptr.next = pre_ptr.next
                pre_ptr.next = cur_ptr
                cur_ptr = last_pre.next
            else:
                if not pre_ptr:
                    last_pre.next = cur_ptr.next
                    cur_ptr.next = head
                    head = cur_ptr
                    cur_ptr = last_pre.next
                else:
                    last_pre = cur_ptr
                    cur_ptr = cur_ptr.next

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
            line = sys.stdin.readline().rstrip('\n')
            head = stringToListNode(line)

            ret = Solution().insertionSortList(head)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
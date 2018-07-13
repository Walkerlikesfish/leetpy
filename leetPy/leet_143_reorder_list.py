# Definition for singly-linked list.
import json

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        cnt_n = 0
        cur_ptr = head
        node_list = []
        while cur_ptr:
            node_list.append(cur_ptr)
            cnt_n += 1
            cur_ptr = cur_ptr.next

        n = cnt_n
        cnt_n = 0
        cur_ptr = head
        while cnt_n < n/2:
            cnt_n += 1
            cur_nxt_ptr = node_list[n - cnt_n]
            cur_nxt_nxt_ptr = cur_ptr.next
            if cur_nxt_nxt_ptr == cur_nxt_ptr:
                cur_nxt_ptr.next = None
                return
            cur_ptr.next = cur_nxt_ptr
            cur_nxt_ptr.next = cur_nxt_nxt_ptr
            cur_ptr = cur_nxt_nxt_ptr
        cur_ptr.next = None


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

            ret = Solution().reorderList(head)

            out = listNodeToString(head)
            if ret is not None:
                print "Do not return anything, modify head in-place instead."
            else:
                print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
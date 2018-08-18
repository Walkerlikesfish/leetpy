# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import json

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        pre_pre_ptr = ListNode(0)
        pre_pre_ptr.next = head
        headh = pre_pre_ptr
        pre_ptr = head
        cur_ptr = head.next

        dupli = False

        while cur_ptr is not None:
            if cur_ptr.val == pre_ptr.val:
                pre_ptr.next = cur_ptr.next
                dupli = True
            else:
                if dupli:
                    dupli = False
                    pre_pre_ptr.next = cur_ptr
                else:
                    pre_pre_ptr = pre_pre_ptr.next
                pre_ptr = cur_ptr
            cur_ptr = cur_ptr.next
        if dupli:
            pre_pre_ptr.next = cur_ptr

        return headh.next



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
            line = sys.stdin.readline().strip('\n')
            head = stringToListNode(line)

            ret = Solution().deleteDuplicates(head)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
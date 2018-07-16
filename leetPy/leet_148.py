# Definition for singly-linked list.
import json

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    '''
    Use merge sort to do the sorting
    '''
    def mergeList(self, head1, head2):
        headhead = ListNode(0)
        cur_ptr = headhead
        while head1 and head2:
            if head1.val <= head2.val:
                cur_ptr.next = head1
                head1 = head1.next
                cur_ptr = cur_ptr.next
            else:
                cur_ptr.next = head2
                head2 = head2.next
                cur_ptr = cur_ptr.next
        if head1:
            cur_ptr.next = head1
            # while head1:
            #     cur_ptr.next = head1
            #     head1 = head1.next
        if head2:
            cur_ptr.next = head2
            # while head2:
            #     cur_ptr.next = head2
            #     head2 = head2.next

        return headhead.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # use fast/slow ptr to half the list
        if not head or not head.next:
            return head
        ptr_1 = head
        ptr_2 = head
        while ptr_1.next and ptr_1.next.next:
            ptr_1 = ptr_1.next.next
            ptr_2 = ptr_2.next
        head1 = head
        head2 = ptr_2.next
        ptr_2.next = None
        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        return self.mergeList(head1, head2)


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

            ret = Solution().sortList(head)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
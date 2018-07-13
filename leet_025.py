# Definition for singly-linked list.
import json

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        headhead = ListNode(0)
        headhead.next = head

        ptr_pre = headhead
        ptr_cur = ptr_pre.next

        lnt = 0
        while ptr_cur is not None:
            lnt += 1
            ptr_cur = ptr_cur.next
        if lnt < k:
            return head

        ptr_cur = ptr_pre.next

        cnt = 0
        while ptr_cur is not None:
            # print ptr_cur.val

            if cnt % k == 0:
                if (lnt-cnt)/k == 0:
                    ptr_pre.next = ptr_cur
                    break
                ptr_to_go = ptr_cur.next
                ptr_0 = ptr_cur
                ptr_0_pre = ptr_pre
                ptr_pre = ptr_cur

                ptr_cur = ptr_to_go
            elif cnt%k < k-1:
                ptr_to_go = ptr_cur.next
                ptr_cur.next = ptr_pre
                ptr_pre = ptr_cur
                ptr_cur = ptr_to_go
            else:
                ptr_to_go = ptr_cur.next
                ptr_cur.next = ptr_pre
                ptr_pre = ptr_0
                ptr_0.next = ptr_to_go
                ptr_0_pre.next  = ptr_cur

                ptr_cur = ptr_to_go
            cnt += 1

        # if cnt != 0:
        #     print ptr_pre.val
        #     ptr_pre.next = None

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

            ret = Solution().reverseKGroup(head, k)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
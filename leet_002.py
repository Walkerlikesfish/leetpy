import json

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ptr1 = l1
        ptr2 = l2
        resultRoot = ListNode(0)
        ptrR = resultRoot
        curC = 0
        nxtC = 0
        while (ptr1 is not None or ptr2 is not None or curC>0):
            if ptr1 is None:
                cur1 = 0
            else:
                cur1 = ptr1.val
                ptr1 = ptr1.next
            if ptr2 is None:
                cur2 = 0
            else:
                cur2 = ptr2.val
                ptr2 = ptr2.next
            curD = int((cur1+cur2+curC)%10)
            nxtC = int((cur1+cur2+curC)/10)

            # record current Digits
            ptrR.next = ListNode(curD)
            ptrR = ptrR.next

            # update Carry
            curC = nxtC

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
    # def readlines():
    #     for line in sys.stdin:
    #         yield line.strip('\n')
    #
    # lines = readlines()

    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            l1 = stringToListNode(line)
            line = sys.stdin.readline().rstrip('\n')
            l2 = stringToListNode(line)

            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
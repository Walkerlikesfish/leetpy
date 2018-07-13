# Definition for singly-linked list.
import json

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """

        :param lists:
        :return:
        """
        if len(lists) == 0:
            return []
        return self.mergeKLists_b(lists, 0, len(lists)-1)

    def mergeKLists_b(self, lists, a, b):
        if a<b:
            mid = (a+b)/2
            return self.merge2Lists(self.mergeKLists_b(lists,a,mid), self.mergeKLists_b(lists, mid+1, b))
        else:
            return lists[a]

    def merge2Lists(self, list_a, list_b):
        result = ListNode(0)
        ptr_r = result
        ptr_a = list_a
        ptr_b = list_b
        while ptr_a is not None and ptr_b is not None:
            if ptr_a.val < ptr_b.val:
                ptr_r.next = ListNode(ptr_a.val)
                ptr_r = ptr_r.next
                ptr_a = ptr_a.next
            else:
                ptr_r.next = ListNode(ptr_b.val)
                ptr_r = ptr_r.next
                ptr_b = ptr_b.next
        if ptr_a is None:
            ptr_r.next = ptr_b
        if ptr_b is None:
            ptr_r.next = ptr_a

        return result.next


    def mergeKLists_naive(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        result = ListNode(0)
        rptr = result
        finished = False
        hptrs = lists
        while not finished:
            cur_min = 1000000
            ind_min = 0
            finished = True
            for i, hptr in enumerate(hptrs):
                if hptr is not None:
                    finished = False
                    if hptr.val < cur_min:
                        cur_min = hptr.val
                        ind_min = i
            if not finished:
                rptr.next = ListNode(cur_min)
                rptr = rptr.next
                hptrs[ind_min] = hptrs[ind_min].next

        return result.next


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


def stringToListNodeArray(input):
    listNodeArrays = json.loads(input)
    nodes = []
    for listNodeArray in listNodeArrays:
        nodes.append(stringToListNode(json.dumps(listNodeArray)))
    return nodes


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
            lists = stringToListNodeArray(line)

            ret = Solution().mergeKLists(lists)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
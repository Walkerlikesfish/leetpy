import json

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def add(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            cur_ptr = self.root
            prev_ptr = None
            while cur_ptr:
                if val < cur_ptr.val:
                    cur_ptr = cur_ptr.left
                    prev_ptr = cur_ptr
                elif val > cur_ptr.val:
                    cur_ptr = cur_ptr.right
                    prev_ptr = cur_ptr
                else:
                    return self.root
            if val < prev_ptr.val:
                prev_ptr.left = TreeNode(val)
            else:
                prev_ptr.right = TreeNode(val)

    def search(self, targ):
        cur_ptr = self.root
        while cur_ptr:
            if cur_ptr.val == targ:
                return cur_ptr
            elif cur_ptr.val < targ:
                cur_ptr = cur_ptr.right
            else:
                cur_ptr = cur_ptr.left
        return None

    def node_ceil(self, ptr_t):
        """

        :param ptr_t:
        :return: ceil_node: node,
        """
        if ptr_t:
            cur_ptr = ptr_t.right
            if cur_ptr:
                while cur_ptr.left:
                    cur_ptr = cur_ptr.left
            return cur_ptr
        return None

    def node_floor(self, ptr_t):
        if ptr_t:
            cur_ptr = ptr_t.left
            if cur_ptr:
                while cur_ptr.right:
                    cur_ptr = cur_ptr.right
            return cur_ptr
        return None


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """


def stringToIntegerList(input):
    return json.loads(input)


def stringToInt(input):
    return int(input)


def main():
    import sys

    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            nums = stringToIntegerList(line)
            line = sys.stdin.readline().rstrip('\n')
            k = stringToInt(line)
            line = sys.stdin.readline().rstrip('\n')
            t = stringToInt(line)

            ret = Solution().containsNearbyAlmostDuplicate(nums, k, t)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
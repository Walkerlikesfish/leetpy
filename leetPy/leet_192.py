import json


class TNode(object):
    def __init__(self):
        self.children = {}  # 0,1


class Trie(object):
    def __init__(self):
        self.head = TNode()

    def insert_number(self, n):
        cur_ptr = self.head
        for ibit in range(32, 0, -1):
            cur_bit = n >> (ibit - 1) & 1
            if cur_bit not in cur_ptr.children:
                cur_ptr.children[cur_bit] = TNode()
            cur_ptr = cur_ptr.children[cur_bit]

    def search_largest_xor(self, n):
        cur_ptr = self.head
        val_sum = 0
        for ibit in range(32, 0, -1):
            cur_bit = n >> (ibit - 1) & 1
            if cur_bit ^ 1 not in cur_ptr.children:
                cur_ptr = cur_ptr.children[cur_bit]
            else:
                val_sum += 1 << (ibit - 1)
                cur_ptr = cur_ptr.children[cur_bit ^ 1]
        return val_sum


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        # init the Trie
        t = Trie()
        for each_num in nums:
            t.insert_number(each_num)
        # search the Trie
        res = 0
        for each_num in nums:
            res = max(res, t.search_largest_xor(each_num))
        return res


def stringToIntegerList(input):
    return json.loads(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = sys.stdin.readline().strip('\n')
            nums = stringToIntegerList(line)

            ret = Solution().findMaximumXOR(nums)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
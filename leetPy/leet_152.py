import json

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        else:
            cur_max = nums[0]
            cur_min = nums[0]
            res = cur_max
            for i, ie in enumerate(nums[1:]):
                tmp = cur_max
                cur_max = max(ie, max(cur_max*ie, cur_min*ie))
                cur_min = min(ie, min(tmp*ie, cur_min*ie))
                res = max(res, cur_max)
        return res


def stringToIntegerList(input):
    return json.loads(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys

    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            nums = stringToIntegerList(line)

            ret = Solution().maxProduct(nums)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
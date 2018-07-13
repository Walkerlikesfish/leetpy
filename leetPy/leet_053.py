import json

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        d = [0]*n
        max_sub = d[0]
        if nums[0]>=0:
            d[0] = nums[0]
        for i in range(1, n):
            if d[i-1] >=0:
                d[i] = d[i-1] + nums[i]
            else:
                d[i] = nums[i]
            max_sub = max(max_sub, d[i])
        return max_sub


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
            line = sys.stdin.readline().rstrip('\n')
            nums = stringToIntegerList(line)

            ret = Solution().maxSubArray(nums)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
import json

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = 3
        res = 0
        for ibit in range(32):
            imask = 1 << ibit
            isum = 0
            for en in nums:
                if en & imask:
                    isum += 1
            isum %= N # will be 1 for the single number
            res += isum << ibit
        if res & (1 << 31):  # sign signal
            res -= 1
            res = ~res
            res = res & ((1 << 31) - 1)
            res = -res
            if res == 0:
                res = -2147483648
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
            line = sys.stdin.readline().rstrip('\n')
            nums = stringToIntegerList(line)

            ret = Solution().singleNumber(nums)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
import json

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        while i<n:
            a = nums[i]
            if a == i+1 or a<1 or a>n or nums[a-1]==a:
                i+=1
            else:
                nums[i],nums[a-1] = nums[a-1], nums[i]
        for i,a in enumerate(nums):
            if a!=i+1:
                return i+1
        return n+1


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

            ret = Solution().firstMissingPositive(nums)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
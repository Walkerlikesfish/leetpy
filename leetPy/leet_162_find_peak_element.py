import json

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        n = len(nums)
        if n == 1:
            return nums[0]
        left = 0
        right = n-1
        while left < right:
            if left == right:
                return left
            mid = (left + right)/2
            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid
        return left



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

            ret = Solution().findPeakElement(nums)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
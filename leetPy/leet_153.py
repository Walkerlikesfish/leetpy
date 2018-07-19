import json

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        return self.biFindMin(0, len(nums)-1)

    def biFindMin(self, left, right):
        if left < right:
            mid = (left + right) / 2
            if mid == left:
                return min(self.nums[left], self.nums[right])
            if self.nums[left] == self.nums[mid]:
                tmp = self.nums[mid]
                return min(tmp, min(self.biFindMin(left, mid-1), self.biFindMin(mid+1, right)))
            elif self.nums[left] < self.nums[mid]: # left part is in order
                tmp = self.nums[left]
                return min(tmp, self.biFindMin(mid+1, right))
            else: # right part is in order
                tmp = self.nums[mid]
                return min(tmp, self.biFindMin(left, mid-1))
        elif left == right:
            return self.nums[left]


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

            ret = Solution().findMin(nums)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
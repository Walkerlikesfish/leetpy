import json

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ii = n-1
        if n == 1:
            return
        while nums[ii-1]>=nums[ii] and ii>=0:
            ii -= 1
        i1 = ii-1
        if i1<0:
            nums[:] = reversed(nums[:])
        else:
            while ii<n and nums[ii]>nums[i1]:
                ii += 1
            # print i1,ii-1
            nums[ii-1],nums[i1] = nums[i1],nums[ii-1]
            nums[i1+1:] = reversed(nums[i1+1:])


def stringToIntegerList(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


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

            ret = Solution().nextPermutation(nums)

            out = integerListToString(nums)
            if ret is not None:
                print "Do not return anything, modify nums in-place instead."
            else:
                print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
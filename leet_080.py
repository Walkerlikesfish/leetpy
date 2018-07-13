import json

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return
        cur_cnt = 1
        pen = nums[0]

        ptri = 1
        while ptri < len(nums):
            if nums[ptri] == nums[ptri-1]:
                cur_cnt += 1
                if cur_cnt > 2:
                    nums.pop(ptri)
                else:
                    ptri+=1
            else:
                cur_cnt = 1
                ptri+=1


def stringToIntegerList(input):
    return json.loads(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


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

            ret = Solution().removeDuplicates(nums)

            out = integerListToString(nums, len_of_list=ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
import json
import sys


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, cur_num in enumerate(nums):
            the_other_num = target - cur_num
            ii = -1
            try:
                ii = nums[i+1:].index(the_other_num)
            except:
                pass
            if ii >= 0:
                return [i, ii+i+1]
            

def stringToIntegerList(input):
    return json.loads(input)

def stringToInt(input):
    return int(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    # import sys
    # def readlines():
    #     for line in sys.stdin:
    #         yield line.strip('\n')
    # lines = readlines()
    while True:
        try:
            #line = lines.next()
            line = sys.stdin.readline().rstrip('\n')
            nums = stringToIntegerList(line)
            #line = lines.next()
            line = sys.stdin.readline().rstrip('\n')
            target = stringToInt(line)
            ret = Solution().twoSum(nums, target)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
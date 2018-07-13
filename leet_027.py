import json

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while True:
            try:
                nums.remove(val)
            except:
                return len(nums)

def stringToIntegerList(input):
    return json.loads(input)


def stringToInt(input):
    return int(input)


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
            line = sys.stdin.readline().rstrip('\n')
            val = stringToInt(line)

            ret = Solution().removeElement(nums, val)

            out = integerListToString(nums, len_of_list=ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
import json

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        t_res = 0
        # get the distinguish mask
        for i_nume, e_n in enumerate(nums):
            t_res ^= e_n
        ct_res = ~t_res + 1
        ct_res &= t_res # this is the mask
        a_val = 0
        b_val = 0
        for _, e_n in enumerate(nums):
            if e_n & ct_res:
                a_val ^= e_n
            else:
                b_val ^= e_n
        return [a_val, b_val]


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

            ret = Solution().singleNumber(nums)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
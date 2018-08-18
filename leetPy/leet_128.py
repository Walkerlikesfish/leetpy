import json

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums_map = {}
        for each in nums:
            nums_map[each] = True

        res = 0

        for each_num in nums:
            a = each_num
            if a in nums_map:
                cnt = 1
                # incremental
                while a+1 in nums_map:
                    a += 1
                    try:
                        nums.remove(a)
                        cnt += 1
                    except ValueError:
                        pass

                a = each_num
                while a-1 in nums_map:
                    a-= 1
                    try:
                        nums.remove(a)
                        cnt += 1
                    except ValueError:
                        pass

                res = max(res, cnt)
                # decremental

        return res


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
            line = sys.stdin.readline().strip('\n')
            nums = stringToIntegerList(line)

            ret = Solution().longestConsecutive(nums)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
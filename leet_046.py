import json


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.results = []
        self.genPermute([], nums)
        return self.results

    def genPermute(self, cur_res, cur_candies):
        if len(cur_candies)>0:
            for ind, cur_cand in enumerate(cur_candies):
                new_candies = list(cur_candies)
                new_candies.pop(ind)
                new_res = list(cur_res)
                new_res.append(cur_cand)
                self.genPermute(new_res, new_candies)
        else:
            self.results.append(cur_res)


def stringToIntegerList(input):
    return json.loads(input)


def int2dArrayToString(input):
    return json.dumps(input)


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

            ret = Solution().permute(nums)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
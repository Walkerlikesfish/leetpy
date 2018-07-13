import json


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.results = []
        self.nums = sorted(nums)
        self.disponible_nums = [True]*len(self.nums)
        self.genPermuteUnique([])
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
            if len(self.results) > 0:
                s = 0
                for i in range(len(self.results)):
                    s = 0
                    for j in range(len(self.results[i])):
                        s += abs(self.results[i][j] - cur_res[j])
                    if s == 0:
                        break
                if s>0:
                    self.results.append(cur_res)
            else:
                self.results.append(cur_res)

    def genPermuteUnique(self, cur_res):
        if len(cur_res) < len(self.nums):
            for i,cur_num in enumerate(self.nums):
                if not self.disponible_nums[i]:
                    continue
                elif i>0 and self.nums[i] == self.nums[i-1] and self.disponible_nums[i-1]: # the num is intended not to use
                    continue
                else:
                    self.disponible_nums[i]=False
                    new_res = list(cur_res)
                    new_res.append(self.nums[i])
                    self.genPermuteUnique(new_res)
                    self.disponible_nums[i]=True
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

            ret = Solution().permuteUnique(nums)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
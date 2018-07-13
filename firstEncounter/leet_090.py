import json

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = []
        self.n = len(nums)
        self.res = []
        self.cntb = {}

        for en in nums:
            if en not in self.cntb:
                self.cntb[en] = 1
                self.nums.append(en)
            else:
                self.cntb[en] += 1
        self.genSub(0, {})
        return self.res

    def genSub(self, cur_id, cur_cnt):
        if cur_id < len(self.nums):
            cur_top = self.cntb[self.nums[cur_id]]
            for ea in range(cur_top+1):
                new_cnt = dict(cur_cnt)
                new_cnt[self.nums[cur_id]] = ea
                # print new_cnt
                self.genSub(cur_id+1, new_cnt)
        else:
            tmp = []
            for ekey in cur_cnt:
                tmp.extend([ekey]*cur_cnt[ekey])
            print tmp
            self.res.append(tmp)



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

            ret = Solution().subsetsWithDup(nums)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
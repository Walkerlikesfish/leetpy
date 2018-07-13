import json


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.candies = sorted(candidates)
        self.tango = target
        self.reuslts = []
        self.genCombine(0, 0, [])
        return self.reuslts

    def genCombine(self, cur_ind, cur_sum, cur_list):
        if cur_ind < len(self.candies):
            if cur_sum <= self.tango:
                # add number in this ind
                new_list = list(cur_list)
                new_list.append(self.candies[cur_ind])
                self.genCombine(cur_ind+1, cur_sum+self.candies[cur_ind], new_list)
                # DONOT add this number
                self.genCombine(cur_ind+1, cur_sum, cur_list)
        else:
            if cur_sum == self.tango:
                if not cur_list in self.reuslts:
                    self.reuslts.append(cur_list)


def stringToIntegerList(input):
    return json.loads(input)


def stringToInt(input):
    return int(input)


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
            candidates = stringToIntegerList(line)
            line = sys.stdin.readline().rstrip('\n')
            target = stringToInt(line)

            ret = Solution().combinationSum2(candidates, target)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
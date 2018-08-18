import json

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.candies = candidates
        self.tango = target
        self.candie_nums = [target/x for x in self.candies]
        self.results = []
        self.genCombination(0, 0, [])
        return self.results

    def genCombination(self, cur_ind, cur_sum, cur_re):
        curv = self.candies[cur_ind]
        if cur_ind<len(self.candies)-1:
            cur_nmax = (self.tango-cur_sum)/curv
            for i in xrange(cur_nmax+1):
                cur_re_t = list(cur_re)
                cur_re_t.extend(i*[curv])
                self.genCombination(cur_ind+1, cur_sum+i*curv, cur_re_t)
        else:
            cur_nmax = (self.tango-cur_sum)/curv
            if cur_nmax == 0 and cur_sum == self.tango:
                self.results.append(cur_re)
            else:
                if self.tango-cur_sum-cur_nmax*curv == 0:
                    cur_re_t = list(cur_re)
                    cur_re_t.extend([curv]*cur_nmax)
                    self.results.append(cur_re_t)




def stringToIntegerList(input):
    return json.loads(input)


def stringToInt(input):
    return int(input)


def int2dArrayToString(input):
    return json.dumps(input)


def main():
    import sys

    while True:
        try:
            line = sys.stdin.readline().strip('\n')
            candidates = stringToIntegerList(line)
            line = sys.stdin.readline().strip('\n')
            target = stringToInt(line)

            ret = Solution().combinationSum(candidates, target)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
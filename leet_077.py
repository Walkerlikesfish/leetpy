import json

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.n = n
        self.k = k
        self.res = []
        self.genCombine(1, [])
        return self.res

    def genCombine(self, cur_n, cur_v):
        if cur_n <= self.n+1:
            if len(cur_v) == self.k:
                self.res.append(cur_v)
            else:
                new_v = list(cur_v)
                self.genCombine(cur_n+1, new_v)
                new_v.append(cur_n)
                self.genCombine(cur_n+1, new_v)
        else:
            return


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
            n = stringToInt(line)
            line = sys.stdin.readline().rstrip('\n')
            k = stringToInt(line)

            ret = Solution().combine(n, k)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
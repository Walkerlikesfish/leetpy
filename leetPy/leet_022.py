import json

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.n = n
        self.s = []
        self.result = []
        self.genp(pcnt=0, pcur=0, cur_s='')
        return self.result

    def genp(self, pcur, pcnt, cur_s):
        if pcnt == self.n:
            while pcur>0:
                pcur -= 1
                cur_s += ')'
            self.result.append(cur_s)
        else:
            self.genp(pcur=pcur+1, pcnt=pcnt+1, cur_s=(cur_s+'('))
            if pcur > 0:
                self.genp(pcur=pcur-1, pcnt=pcnt, cur_s=(cur_s+')'))


def stringToInt(input):
    return int(input)


def stringArrayToString(input):
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

            ret = Solution().generateParenthesis(n)

            out = stringArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
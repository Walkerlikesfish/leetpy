import numpy as np
import json
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        self.K = K
        self.quality = quality
        self.wage = wage
        self.nworker = len(quality)
        self.res = self.calcTotal(self.quality, self.wage)

        if len(quality) == self.K:
            return self.res
        else:
            self.recFindWorker([],[],0)
            return self.res

    def recFindWorker(self, cur_q, cur_w, cur_n):
        if len(cur_q) == self.K:
            tmpw = self.calcTotal(cur_q, cur_w)
            self.res = min(self.res, tmpw)
        elif cur_n < self.nworker:
            new_w = list(cur_w)
            new_q = list(cur_q)
            self.recFindWorker(new_w, new_w, cur_n + 1)
            new_q.append(self.quality[cur_n])
            new_w.append(self.wage[cur_n])
            tmpt = self.calcTotal(new_q, new_w)
            if tmpt > self.res:
                return
            else:
                self.recFindWorker(new_w, new_w, cur_n + 1)


    def calcTotal(self, quality, wage):
        quality = np.array(quality)
        wage = np.array(wage)
        qmin = np.min(quality)
        iqmin = np.argmin(quality)
        wmin = wage[iqmin]
        swage = 0

        for eq in quality:
            eq = eq/qmin
            swage += eq * wmin

        return swage


def stringToIntegerList(input):
    return json.loads(input)


def stringToInt(input):
    return int(input)


def doubleToString(input):
    if input is None:
        input = 0
    return "%.5f" % input


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            quality = stringToIntegerList(line)
            line = sys.stdin.readline().rstrip('\n')
            wage = stringToIntegerList(line)
            line = sys.stdin.readline().rstrip('\n')
            K = stringToInt(line)

            ret = Solution().mincostToHireWorkers(quality, wage, K)

            out = doubleToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
import json


class Solution(object):
    def maxProfit_2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        n = len(prices)
        res = 0
        pbase = prices[0]
        for iep,ep in enumerate(prices):
            if ep > pbase:
                lp = ep-pbase
                rp = self.getProfit(prices[iep+1:])
                if lp+rp > res:
                    res = lp+rp
            else:
                pbase = min(pbase, ep)
        return res

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        n = len(prices)
        res = 0
        # calc forward to get profit at each point
        profit_record = [0]
        pbase = prices[0]
        for iep,ep in enumerate(prices[1:]):
            pbase = min(pbase, ep)
            profit_record.append(max(ep-pbase, profit_record[-1]))
        # calc backward to get the sum of two purchase
        print profit_record
        pbase = prices[-1]
        res = max(profit_record)
        for iep in range(n-2, 0, -1):
            if prices[iep] > pbase:
                pbase = prices[iep]
            else:
                res = max(res,  pbase - prices[iep] + profit_record[iep-1])
        return res

    def getProfit(self, prices):
        if len(prices) < 2:
            return 0
        else:
            pbase = prices[0]
            res = 0
            for ep in prices:
                if ep > pbase:
                   res = max(res, ep-pbase)
                else:
                    pbase = min(pbase, ep)
            return res


def stringToIntegerList(input):
    return json.loads(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = sys.stdin.readline().strip('\n')
            prices = stringToIntegerList(line)

            ret = Solution().maxProfit(prices)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
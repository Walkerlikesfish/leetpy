import json

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minp = prices[0]
        res = 0
        for ep in prices:
            if ep < minp:
                minp = ep
            else:
                res = max(res, ep-minp)
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
            prices = stringToIntegerList(line)

            ret = Solution().maxProfit(prices)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
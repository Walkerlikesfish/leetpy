import json

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        res = 0
        n = len(ratings)
        candya = [1] * n
        candyb = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candya[i] = candya[i-1]+1
            else:
                candya[i] = 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candyb[i] = candyb[i+1] + 1
            res += max(candyb[i], candya[i])

        res += max(candyb[n-1],candya[n-1])
        print candya,candyb
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
            line = sys.stdin.readline().rstrip('\n')
            ratings = stringToIntegerList(line)

            ret = Solution().candy(ratings)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
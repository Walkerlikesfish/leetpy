class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = [0]*(n+1)
        d[1] = 1
        d[0] = 1
        for i in range(2,n+1):
            d[i] = d[i-1]+d[i-2]
        return d[n]


def stringToInt(input):
    return int(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys

    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            n = stringToInt(line)

            ret = Solution().climbStairs(n)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
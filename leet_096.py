class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]*(n+1)
        dp[0]=1
        for i in range(1,n+1):
            for j in range(i):
                dp[i]+=dp[j]*dp[i-1-j]
        return dp[n]


def stringToInt(input):
    return int(input)


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
            line = sys.stdin.readline().rstrip('\n')
            n = stringToInt(line)

            ret = Solution().numTrees(n)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
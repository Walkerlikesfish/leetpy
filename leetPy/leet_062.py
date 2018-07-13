import numpy as np
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        d = np.zeros((m,n), dtype=np.int64)
        d[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i>0:
                    d[i][j] += d[i-1][j]
                if j>0:
                    d[i][j] += d[i][j-1]
        return d[m-1][n-1]


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
            m = stringToInt(line)
            line = sys.stdin.readline().rstrip('\n')
            n = stringToInt(line)

            ret = Solution().uniquePaths(m, n)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
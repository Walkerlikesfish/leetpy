import json

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)

        d = [[0]*(m+1) for _ in range(n+1)]

        # init the state mat
        d[0][0] = 0
        for i in range(1,m+1):
            d[0][i] = i
        for i in range(1, n+1):
            d[i][0] = i

        # update state
        for i in range(1, n+1):
            for j in range(1, m+1):
                v = 0 if word1[i-1]==word2[j-1] else 1
                d[i][j] = min(
                    d[i][j-1]+1,
                    d[i-1][j]+1,
                    d[i-1][j-1]+v
                )

        return d[n][m]


def stringToString(input):
    return input[1:-1].decode('string_escape')


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
            word1 = stringToString(line)
            line = sys.stdin.readline().rstrip('\n')
            word2 = stringToString(line)

            ret = Solution().minDistance(word1, word2)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
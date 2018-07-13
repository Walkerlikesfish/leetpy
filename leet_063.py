import json

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        d = [[0]*n for _ in range(m)]
        d[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    if i>0:
                        d[i][j] += d[i-1][j]
                    if j>0:
                        d[i][j] += d[i][j-1]
                else:
                    d[i][j] = 0
        return d[m-1][n-1]


def stringToInt2dArray(input):
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
            obstacleGrid = stringToInt2dArray(line)

            ret = Solution().uniquePathsWithObstacles(obstacleGrid)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
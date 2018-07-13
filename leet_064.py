import json

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        d = [[0]*n for _ in range(m)]
        d[0][0] = 0

        for i in range(m):
            for j in range(n):
                if i==0 and j>0:
                    d[i][j] = d[i][j-1]+grid[i][j]
                elif j==0 and i>0:
                    d[i][j] = d[i-1][j]+grid[i][j]
                else:
                    d[i][j] = min(d[i-1][j],d[i][j-1])+grid[i][j]

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
            grid = stringToInt2dArray(line)

            ret = Solution().minPathSum(grid)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
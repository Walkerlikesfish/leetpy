import json

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        n_m = len(dungeon)
        n_n = len(dungeon[0])

        d = [[0]*n_n for _ in range(n_m)]

        d[n_m-1][n_n-1] = max(1-dungeon[n_m-1][n_n-1], 1)

        # two boarder case
        for i in range(n_m-2, -1, -1):
            d[i][n_n-1] = max(d[i+1][n_n-1] - dungeon[i][n_n-1], 1)
        for i in range(n_n-2, -1, -1):
            d[n_m-1][i] = max(d[n_m-1][i+1] - dungeon[n_m-1][i], 1)

        for i in range(n_m-2, -1, -1):
            for j in range(n_n-2, -1, -1):
                patha = max(1, d[i+1][j] - dungeon[i][j])
                pathb = max(1, d[i][j+1] - dungeon[i][j])
                d[i][j] = min(patha, pathb)

        return d[0][0]

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
            dungeon = stringToInt2dArray(line)

            ret = Solution().calculateMinimumHP(dungeon)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
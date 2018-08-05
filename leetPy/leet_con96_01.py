import json

class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n_row = len(grid)
        n_col = len(grid[0])

        cnt = 0

        # xy
        for ir in range(n_row):
            for ic in range(n_col):
                if grid[ir][ic] > 0:
                    cnt += 1

        # xz
        for ir in range(n_row):
            cnt += max(grid[ir])

        # yz
        for ic in range(n_col):
            tmp = []
            for ir in range(n_row):
                tmp.append(grid[ir][ic])
            cnt += max(tmp)

        return cnt



def stringToInt2dArray(input):
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
            line = sys.stdin.readline().rstrip('\n')
            grid = stringToInt2dArray(line)

            ret = Solution().projectionArea(grid)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
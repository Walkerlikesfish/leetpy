import json

class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nr = len(grid)
        nc = len(grid[0])

        cnt = 0
        maxr = []
        maxc = [0] * nc
        north_south = 0
        left_right = 0
        for ir,each_row in enumerate(grid):
            if ir == 0:
                north_south += sum(each_row)
            if ir == nr-1:
                north_south += sum(each_row)
            if ir < nr-1:
                for ia,a in enumerate(each_row):
                    if grid[ir+1][ia]-a> 0:
                        north_south += grid[ir+1][ia]-a
            if ir > 0:
                # dif_row = grid[ir-1] - each_row
                for ia, a in enumerate(each_row):
                    if grid[ir-1][ia]-a> 0:
                        north_south += grid[ir-1][ia]-a
            for ic,each_c in enumerate(each_row):
                if each_c>0:
                    cnt += 1
                if ic == 0:
                    left_right += each_c
                if ic < nc-1 and each_row[ic+1] - each_c > 0:
                    left_right += each_row[ic+1] - each_c
                if ic == nc-1:
                    left_right += each_c
                if ic >0 and each_row[ic-1] - each_c > 0:
                    left_right += each_row[ic-1] - each_c

        up_down = cnt * 2
        print up_down, left_right, north_south
        # east_west = sum(maxr) * 2
        # north_south = sum(maxc) * 2

        res = up_down + left_right + north_south

        return res


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

            ret = Solution().surfaceArea(grid)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
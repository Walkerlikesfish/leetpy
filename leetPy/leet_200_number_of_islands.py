import json
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        nr = len(grid)
        nc = len(grid[0])
        cnt = 0
        for ir in range(nr):
            for ic in range(nc):
                if grid[ir][ic] == '1':
                    sq = [(ir, ic)]
                    cnt += 1
                    while sq:
                        [cx, cy] = sq.pop()
                        grid[cx][cy] = '0'
                        if cx > 0 and grid[cx-1][cy] == '1':
                            sq.append((cx-1, cy))
                        if cy > 0 and grid[cx][cy-1] == '1':
                            sq.append((cx, cy-1))
                        if cx < nr-1 and grid[cx+1][cy] == '1':
                            sq.append((cx+1, cy))
                        if cy < nc-1 and grid[cx][cy+1] == '1':
                            sq.append((cx, cy+1))
        return cnt

def stringToChar2dArray(input):
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
            grid = stringToChar2dArray(line)

            ret = Solution().numIslands(grid)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
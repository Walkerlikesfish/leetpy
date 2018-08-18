import json

import numpy as np
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rsum = np.zeros((10,10))
        csum = np.zeros((10,10))
        bsum = np.zeros((3,3,10))

        valid = True

        for irow, eachline in enumerate(board):
            for icol, eachele in enumerate(eachline):
                if eachele == ".":
                    vint = 0
                else:
                    vint = int(eachele)
                    if rsum[irow,vint] > 0:
                        return False
                    else:
                        rsum[irow,vint] = 1
                    if csum[icol,vint] > 0:
                        return False
                    else:
                        csum[icol,vint] = 1
                    if bsum[irow/3,icol/3,vint] > 0:
                        return False
                    else:
                        bsum[irow/3,icol/3,vint] = 1

        return True


def stringToChar2dArray(input):
    return json.loads(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = sys.stdin.readline().strip('\n')
            board = stringToChar2dArray(line)

            ret = Solution().isValidSudoku(board)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
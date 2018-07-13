import json
import numpy as np


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        re = []
        for i in range(n):
            re.append([0]*n)

        idirect = 0
        curv = 1
        finished = False
        ix = 0
        iy = 0
        cnt_turn = 0
        while not finished:

            if idirect == 0:
                if iy < n and re[ix][iy] == 0:
                    cnt_turn = 0
                    re[ix][iy] = curv
                    curv += 1
                    iy += 1
                else:
                    idirect = (idirect+1)%4
                    iy -= 1
                    ix += 1
                    if cnt_turn>0:
                        finished = True
                        break
                    cnt_turn += 1
            elif idirect == 1:
                if ix < n and re[ix][iy] == 0:
                    re[ix][iy] = curv
                    curv += 1
                    ix += 1
                    cnt_turn = 0
                else:
                    idirect = (idirect+1)%4
                    ix -= 1
                    iy -= 1
                    if cnt_turn>0:
                        finished = True
                        break
                    cnt_turn += 1
            elif idirect == 2:
                if iy >= 0 and re[ix][iy] == 0:
                    re[ix][iy] = curv
                    curv += 1
                    iy -= 1
                    cnt_turn = 0
                else:
                    idirect = (idirect+1)%4
                    ix -= 1
                    iy += 1
                    if cnt_turn>0:
                        finished = True
                        break
                    cnt_turn += 1
            elif idirect == 3:
                if ix >= 0 and re[ix][iy] == 0:
                    re[ix][iy] = curv
                    curv += 1
                    ix -= 1
                    cnt_turn = 0
                else:
                    idirect = (idirect+1)%4
                    ix += 1
                    iy += 1
                    if cnt_turn>0:
                        finished = True
                        break
                    cnt_turn += 1
        return re


def stringToInt(input):
    return int(input)


def int2dArrayToString(input):
    return json.dumps(input)


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

            ret = Solution().generateMatrix(n)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
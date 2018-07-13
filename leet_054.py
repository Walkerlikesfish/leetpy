import json
import numpy as np


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        finished = False
        cur_direct = 0
        nrow = len(matrix)
        if nrow == 0:
            return []
        ncol = len(matrix[0])
        visited = [[False]*ncol]*nrow
        visited = np.array(visited)
        out_array = []
        out_array.append(matrix[0][0])
        visited[0,0] = True
        irow = 0
        icol = 1
        nturn = 0

        while not finished:
            if cur_direct == 0:
                if icol<ncol and visited[irow, icol] == False:
                    visited[irow, icol] = True
                    out_array.append(matrix[irow][icol])
                    icol += 1
                    nturn = 0
                else:
                    nturn+=1
                    if nturn >=2:
                        finished = True
                        break
                    icol -= 1
                    irow += 1
                    cur_direct = (cur_direct+1)%4

            elif cur_direct == 1:
                if irow < nrow and visited[irow, icol] != True:
                    visited[irow, icol] = True
                    out_array.append(matrix[irow][icol])
                    irow += 1
                    nturn = 0
                else:
                    nturn += 1
                    if nturn >= 2:
                        finished = True
                        break
                    irow -= 1
                    icol -= 1
                    cur_direct = (cur_direct + 1) % 4

            elif cur_direct == 2:
                if icol > -1 and visited[irow, icol] != True:
                    visited[irow, icol] = True
                    out_array.append(matrix[irow][icol])
                    icol -= 1
                    nturn = 0
                else:
                    nturn += 1
                    if nturn >= 2:
                        finished = True
                        break
                    icol += 1
                    irow -= 1
                    cur_direct = (cur_direct + 1) % 4

            elif cur_direct == 3:
                if irow > -1 and visited[irow, icol] != True:
                    visited[irow, icol] = True
                    out_array.append(matrix[irow][icol])
                    irow -= 1
                    nturn = 0
                else:
                    nturn += 1
                    if nturn >= 2:
                        finished = True
                        break
                    irow += 1
                    icol += 1
                    cur_direct = (cur_direct + 1) % 4

        return out_array


def stringToInt2dArray(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:

            line = sys.stdin.readline().rstrip('\n')
            matrix = stringToInt2dArray(line)

            ret = Solution().spiralOrder(matrix)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
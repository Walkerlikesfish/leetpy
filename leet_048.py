import json

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        1 2 3     7 8 9
        4 5 6 ->  4 5 6 ->
        7 8 9     1 2 3
        """
        nrow = len(matrix)-1
        for irow in range(nrow/2+1):
            matrix[irow], matrix[nrow-irow] = matrix[nrow-irow], matrix[irow]

        for irow in range(nrow+1):
            for icol in range(irow, nrow+1):
                if irow != icol:
                    matrix[irow][icol], matrix[icol][irow] = matrix[icol][irow], matrix[irow][icol]

def stringToInt2dArray(input):
    return json.loads(input)


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
            matrix = stringToInt2dArray(line)

            ret = Solution().rotate(matrix)

            out = int2dArrayToString(matrix)
            if ret is not None:
                print "Do not return anything, modify matrix in-place instead."
            else:
                print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
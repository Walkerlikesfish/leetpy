import json

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        vi = 0
        vj = 0
        for i in range(0,n):
            if matrix[i][0] == 0:
                vi = 1
                break
        for j in range(0,m):
            if matrix[0][j] == 0:
                vj = 1
                break

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1,n):
            if matrix[i][0] == 0:
                matrix[i] = [0]*m
        for j in range(1,m):
            if matrix[0][j] == 0:
                for i in range(0,n):
                    matrix[i][j] = 0
        if vi == 1:
            for i in range(0,n):
                matrix[i][0] = 0
        if vj == 1:
            matrix[0] = [0]*m


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

            ret = Solution().setZeroes(matrix)

            out = int2dArrayToString(matrix)
            if ret is not None:
                print "Do not return anything, modify matrix in-place instead."
            else:
                print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
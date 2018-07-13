import json

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n_row = len(matrix)
        if n_row == 0:
            return False
        n_col = len(matrix[0])
        if n_col == 0:
            return False

        # find the row
        start = 0
        last = n_row-1
        while start<=last:
            mid = (start+last)/2
            if target > matrix[mid][0]:
                start = mid+1
            elif target == matrix[mid][0]:
                return True
            else:
                last = mid-1

        t_row = last
        # find the col
        start = 0
        last = n_col-1
        while start<=last:
            mid = (start+last)/2
            if target > matrix[t_row][mid]:
                start = mid+1
            elif target == matrix[t_row][mid]:
                return True
            else:
                last = mid-1

        return False


def stringToInt2dArray(input):
    return json.loads(input)


def stringToInt(input):
    return int(input)


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
            line = sys.stdin.readline().rstrip('\n')
            target = stringToInt(line)

            ret = Solution().searchMatrix(matrix, target)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
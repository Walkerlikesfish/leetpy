import json

import numpy as np
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A:
            return []
        B = []
        for i in range(len(A)):
            for j in range(0, len(A[0])):
                if i == 0:
                    B.append([A[i][j]])
                else:
                    B[j].append(A[i][j])
        return B

def stringToInt2dArray(input):
    return json.loads(input)


def int2dArrayToString(input):
    return json.dumps(input)


def main():
    import sys

    while True:
        try:
            line = sys.stdin.readline().strip('\n')
            A = stringToInt2dArray(line)

            ret = Solution().transpose(A)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
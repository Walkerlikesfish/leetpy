import json
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]

        For Gray Code:

        1. n <- n-1 series of *n* can be generated from *n-1*

        """
        d = [0, 1, 3, 2]

        if n <= 0:
            return [0]
        if n == 1:
            return [0,1]
        elif n == 2:
            return d
        else:
            for indn in range(3, n+1):
                nd = []
                coef = pow(2, indn-1)
                for ed in d:
                    nd.append(ed)
                for ed in reversed(d):
                    nd.append(coef+ed)
                d = nd
            return d


def stringToInt(input):
    return int(input)


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
            n = stringToInt(line)

            ret = Solution().grayCode(n)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
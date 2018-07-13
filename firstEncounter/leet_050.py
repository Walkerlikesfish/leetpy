import json

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n<0:
            tmp = self.binMyPow(x,-n)
            return 1/tmp
        else:
            return self.binMyPow(x,n)

    def binMyPow(self, x, n):
        if n == 0:
            return 1
        else:
            tmp = self.binMyPow(x, n/2)
            if n%2 == 0:
                return tmp*tmp
            else:
                return tmp*tmp*x


def stringToDouble(input):
    return float(input)


def stringToInt(input):
    return int(input)


def doubleToString(input):
    if input is None:
        input = 0
    return "%.5f" % input


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            x = stringToDouble(line)
            line = sys.stdin.readline().rstrip('\n')
            n = stringToInt(line)

            ret = Solution().myPow(x, n)

            out = doubleToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
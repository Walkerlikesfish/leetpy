class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b != 0:
            carry = a & b
            a = (a ^ b) % 0x100000000
            b = (carry << 1) % 0x100000000
        return a if a <= 0x7FFFFFFF else a | (~0x100000000+1)


def stringToInt(input):
    return int(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys

    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            a = stringToInt(line)
            line = sys.stdin.readline().rstrip('\n')
            b = stringToInt(line)

            ret = Solution().getSum(a, b)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
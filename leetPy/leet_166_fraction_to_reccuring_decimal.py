class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """



def stringToInt(input):
    return int(input)


def main():
    import sys
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            numerator = stringToInt(line)
            line = sys.stdin.readline().rstrip('\n')
            denominator = stringToInt(line)

            ret = Solution().fractionToDecimal(numerator, denominator)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        cur_s = '1'
        for ii in range(n):

    def getNewNumber(self, cur_s):



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
            n = stringToInt(line)

            ret = Solution().countAndSay(n)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
import json

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        


def stringToString(input):
    return input[1:-1].decode('string_escape')


def stringArrayToString(input):
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
            s = stringToString(line)

            ret = Solution().restoreIpAddresses(s)

            out = stringArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
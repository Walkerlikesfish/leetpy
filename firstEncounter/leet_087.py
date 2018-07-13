class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False
        else:
            return self.recIsScramble(s1, s2)

    def recIsScramble(self, s1, s2):
        l = len(s1)
        if l == 0:
            return True
        if l == 1:
            if s1[0] == s2[0]:
                return True
            else:
                return False
        else:
            if sorted(s1) != sorted(s2):
                return False

            for i in range(l-1):
                if self.recIsScramble(s1[0:i+1], s2[0:i+1]) and self.recIsScramble(s1[i+1:], s2[i+1:]):
                    return True
                if self.recIsScramble(s1[0:i+1], s2[-(i+1):]) and self.recIsScramble(s1[i+1:], s2[0:-(i+1)]):
                    return True
            return False



def stringToString(input):
    return input[1:-1].decode('string_escape')


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            s1 = stringToString(line)
            line = sys.stdin.readline().rstrip('\n')
            s2 = stringToString(line)

            ret = Solution().isScramble(s1, s2)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
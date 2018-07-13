import json

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return False
        n = len(s)
        d = [False] * (n+1)
        d[0] = True

        for i in range(n+1):
            for j in range(i):
                if d[j] and s[j:i] in wordDict:
                    d[i] = True

        return d[n]


def stringToString(input):
    return input[1:-1].decode('string_escape')


def stringToStringArray(input):
    return json.loads(input)


def main():
    import sys
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            s = stringToString(line)
            line = sys.stdin.readline().rstrip('\n')
            wordDict = stringToStringArray(line)

            ret = Solution().wordBreak(s, wordDict)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
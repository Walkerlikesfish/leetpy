import json

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        lp = len(pattern)
        res = []
        for w in words:
            fmap = {}  # w[ic] -> p[ic]
            bmap = {}  # p[ic] -> w[ic]
            ispattern = True
            if len(w) != lp:
                continue
            for ic,c in enumerate(pattern):
                cw = w[ic]
                if (cw not in fmap) and (c not in bmap):
                    fmap[cw] = c
                    bmap[c] = cw
                else:
                    if (cw in fmap) and (c in bmap):
                        if fmap[cw] != c or bmap[c] != cw:
                            ispattern = False
                            break
                    else:
                        ispattern = False
                        break
            if ispattern:
                res.append(w)
        return res


def stringToStringArray(input):
    return json.loads(input)


def stringToString(input):
    return input[1:-1].decode('string_escape')


def stringArrayToString(input):
    return json.dumps(input)


def main():
    import sys

    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            words = stringToStringArray(line)
            line = sys.stdin.readline().rstrip('\n')
            pattern = stringToString(line)

            ret = Solution().findAndReplacePattern(words, pattern)

            out = stringArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
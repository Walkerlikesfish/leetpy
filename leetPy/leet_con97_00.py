import json

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        words_map = {}
        words_a = A.split()
        words_b = B.split()
        for ea in words_a:
            if ea not in words_map:
                words_map[ea] = 1
            else:
                words_map[ea] += 1
        for eb in words_b:
            if eb not in words_map:
                words_map[eb] = 1
            else:
                words_map[eb] += 1
        res = []
        for ek in words_map:
            if words_map[ek] == 1:
               res.append(ek)
        return res


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
            A = stringToString(line)
            line = sys.stdin.readline().rstrip('\n')
            B = stringToString(line)

            ret = Solution().uncommonFromSentences(A, B)

            out = stringArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
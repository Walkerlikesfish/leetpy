import json

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return []
        n = len(s)
        d = [False] * (n+1)
        d[0] = True
        res = [[] for _ in range(n+1)]

        for i in range(n+1):
            for j in range(i):
                if d[j] and s[j:i] in wordDict:
                    d[i] = True
                    res[i].append(j)

        self.s = s
        self.wordDict =wordDict
        self.res_cat = []
        self.res = res

        if not d[n]:
            return []
        else:
            # print self.res
            self.tarceBack(n, [])
            return self.res_cat

    def tarceBack(self, ind, cur_res):
        if self.res[ind]:
            for each_pre_ind in self.res[ind]:
                new_res = list(cur_res)
                new_res.append(self.s[each_pre_ind:ind])
                if each_pre_ind == 0:
                    self.res_cat.append(' '.join(new_res[::-1]))
                else:
                    self.tarceBack(each_pre_ind, new_res)



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
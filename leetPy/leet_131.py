import json

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.n = len(s)
        self.res = []
        self.s = s
        if not s:
            return []
        if len(s) == 1:
            return [[s]]

        self.dfs(1, [0])
        return self.res

    def is_hw(self, s):
        # print s
        i = 0
        n = len(s)
        while i<n/2:
            if s[i] != s[n-1-i]:
                return False
            i+=1
        return True

    def dfs(self, cn, cur_set):
        if cn == self.n:
            if len(cur_set)>1 and not self.is_hw(self.s[cur_set[-2]:cur_set[-1]]):
                return
            cur_set.append(cn)
            if not self.is_hw(self.s[cur_set[-2]:cur_set[-1]]):
                return
            else:
                cur_sp = []
                for i in range(1, len(cur_set)):
                    sub_str = self.s[cur_set[i-1]:cur_set[i]]
                    cur_sp.append(sub_str)
                self.res.append(cur_sp)
        else:
            if len(cur_set) > 1:
                if not self.is_hw(self.s[cur_set[-2]:cur_set[-1]]):
                    return
            new_set = list(cur_set)
            new_set.append(cn)
            self.dfs(cn+1, cur_set)
            self.dfs(cn+1, new_set)



def stringToString(input):
    return input[1:-1].decode('string_escape')


def string2dArrayToString(input):
    return json.dumps(input)


def main():
    import sys

    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            s = stringToString(line)

            ret = Solution().partition(s)

            out = string2dArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
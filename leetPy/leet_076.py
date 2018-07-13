class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        nt = len(t)
        ns = len(s)

        # build a hash map for t
        hdict = {}
        for et in t:
            if et in hdict:
                hdict[et] += 1
            else:
                hdict[et] = 1

        # search first round for the left point of the first substring
        ptri = 0
        while ptri < ns:
            if s[ptri] in hdict:
                left = ptri
                break
            ptri += 1

        cnt = 0
        res = ''
        res_cnt = ns
        found = False
        while ptri < ns:
            if s[ptri] in hdict:
                if hdict[s[ptri]] > 0:
                    hdict[s[ptri]] -= 1
                    cnt += 1
                else:
                    hdict[s[ptri]] -= 1
            if cnt == nt:
                while left < ns and (s[left] not in hdict or hdict[s[left]]<0):
                    if s[left] in hdict:
                        hdict[s[left]] += 1
                    left +=1
                if ptri-left < res_cnt:
                    res = s[left:ptri+1]
                    res_cnt = ptri+1-left
                    #print res
                if left < ns:
                    hdict[s[left]] += 1
                    left += 1
                    cnt -= 1
                while left < ns and (s[left] not in hdict or hdict[s[left]]<0):
                    if s[left] in hdict:
                        hdict[s[left]] += 1
                    left +=1
                ptri += 1
            else:
                ptri += 1

        return res

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
            s = stringToString(line)
            line = sys.stdin.readline().rstrip('\n')
            t = stringToString(line)

            ret = Solution().minWindow(s, t)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
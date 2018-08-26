import json

class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        strlist_odd = []
        strlist_even = []
        res = 0
        for ea in A:
            cur_odd = []
            cur_even = []
            for ic,c in enumerate(ea):
                if ic % 2:
                    cur_odd.append(c)
                else:
                    cur_even.append(c)
            cur_odd.sort()
            cur_even.sort()
            if not len(strlist_even):
                strlist_even.append(cur_even)
                strlist_odd.append(cur_odd)
                res += 1
            else:
                f_found = False
                for i in range(len(strlist_even)):
                    if cur_even == strlist_even[i] and cur_odd == strlist_odd[i]:
                        f_found = True

                if not f_found:
                    strlist_odd.append(cur_odd)
                    strlist_even.append(cur_even)
                    res += 1
        #print strlist_even
        #print strlist_odd
        return res



def stringToStringArray(input):
    return json.loads(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            A = stringToStringArray(line)

            ret = Solution().numSpecialEquivGroups(A)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        lA = len(A)
        lB = len(B)
        if lA != lB:
            return False
        else:
            dif_cnt = 0
            p_dif = 0
            rep_tb = [0]*27
            rep_allow = False
            for ia,ea in enumerate(A):
                eb = B[ia]
                cur_dif = ord(ea)-ord(eb)
                if cur_dif != 0:
                    dif_cnt += 1
                    if dif_cnt == 1:
                        p_dif = cur_dif
                    elif dif_cnt == 2:
                        pass
                    else:
                        return False
                else:
                    rep_tb[ord(ea)-97] += 1
                    if rep_tb[ord(ea)-97] > 1:
                        rep_allow = True

            if dif_cnt == 0:
                if rep_allow:  # case 'aa' 'aa'
                    return True
                else:
                    return False
            if dif_cnt == 1:
                return False
            if dif_cnt == 2 and p_dif+cur_dif==0:
                return  True
            else:
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
            A = stringToString(line)
            line = sys.stdin.readline().rstrip('\n')
            B = stringToString(line)

            ret = Solution().buddyStrings(A, B)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
import json

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        st=[[],[],[]]

        for eb in bills:
            if eb == 5:
                st[0].append(eb)
            elif eb == 10:
                if len(st[0]) > 0:
                    st[0].pop()
                    st[1].append(eb)
                else:
                    return False
            elif eb == 20:
                if len(st[0])>0:
                    if len(st[1]) > 0:
                        st[1].pop()
                        st[0].pop()
                        st[2].append(eb)
                    elif len(st[0])>=3:
                        st[0].pop()
                        st[0].pop()
                        st[0].pop()
                        st[2].append(eb)
                    else:
                        return False
                else:
                    return False
        return True


def stringToIntegerList(input):
    return json.loads(input)


def main():
    import sys
    while True:
        try:
            line = sys.stdin.readline().strip('\n')
            bills = stringToIntegerList(line)

            ret = Solution().lemonadeChange(bills)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
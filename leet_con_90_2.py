class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        cur_dir = 0
        cur_pos = 0
        while True:
            # print cur_dir
            if cur_dir == 0 or cur_dir == 1:
                cur_des = cur_pos + q
                if cur_des == p:  # get the corner
                    if cur_dir == 0:
                        return 1
                    elif cur_dir == 1:
                        return 2
                elif cur_des > p:
                    if cur_dir == 0:
                        cur_dir = 3 # change dir
                    elif cur_dir == 1:
                        cur_dir = 2
                    cur_pos = p + (p - cur_des)  # go to the des
                else:
                    if cur_dir == 0:
                        cur_dir = 1
                    elif cur_dir == 1:
                        cur_dir = 0
                    cur_pos = cur_des

            elif cur_dir == 2 or cur_dir == 3:
                cur_des = cur_pos - q
                if cur_des == 0:
                    if cur_dir == 2:
                        return 0
                    else:
                        return -1  # not possible to reflect back to genpoint
                elif cur_des < 0:
                    if cur_dir == 2:
                        cur_dir = 1
                    elif cur_dir == 3:
                        cur_dir = 0
                    cur_pos = -cur_des
                else:
                    if cur_dir == 2:
                        cur_dir = 3
                    elif cur_dir == 3:
                        cur_dir = 2
                    cur_pos = cur_des


def stringToInt(input):
    return int(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            p = stringToInt(line)
            line = sys.stdin.readline().rstrip('\n')
            q = stringToInt(line)

            ret = Solution().mirrorReflection(p, q)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
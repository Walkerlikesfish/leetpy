import json

class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        d = [[0]*C for x in range(R)]
        res = []
        tcnt = 1
        TESTI = R * C
        # control the direction
        cur_cnt = 0
        cur_esti = 1
        esti_cnt = 0

        cx = r0
        cc = c0
        # current direction state
        cs = 0  # right:0 , down:1, left:2, up:3
        while tcnt <= TESTI:
            if cx>-1 and cx < R and cc>-1 and cc < C:
                d[cx][cc] = tcnt
                res.append([cx, cc])
                tcnt += 1

            if cs == 0:
                cc += 1 # go right 1 step
            elif cs == 1:
                cx += 1 # go down 1 step
            elif cs == 2:
                cc -= 1 # go left
            elif cs == 3:
                cx -= 1 # go up

            cur_cnt += 1
            if cur_cnt % cur_esti == 0:
                # turn direction
                cs = (cs+1) % 4
                cur_cnt = 0
                esti_cnt += 1
                # count the turns
                if esti_cnt == 2:
                    cur_esti += 1
                    esti_cnt = 0

        return res

def stringToInt(input):
    return int(input)


def int2dArrayToString(input):
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
            R = stringToInt(line)
            line = sys.stdin.readline().rstrip('\n')
            C = stringToInt(line)
            line = sys.stdin.readline().rstrip('\n')
            r0 = stringToInt(line)
            line = sys.stdin.readline().rstrip('\n')
            c0 = stringToInt(line)

            ret = Solution().spiralMatrixIII(R, C, r0, c0)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
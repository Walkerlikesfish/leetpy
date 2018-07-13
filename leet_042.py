import json

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res_water = 0
        hlen = len(height)
        leftmax = [0]*hlen
        rightmax = [0]*hlen
        if hlen == 0:
            return res_water
        # get the left max and right max for each element
        leftmax[0] = height[0]
        for i in range(1,hlen):
            leftmax[i] = max(leftmax[i-1], height[i])

        rightmax[hlen-1] = height[hlen-1]
        for i in range(hlen-2, -1, -1):
            rightmax[i] = max(rightmax[i+1], height[i])

        for i in range(0, hlen):
            res_water += (min(leftmax[i], rightmax[i]) - height[i])

        print leftmax
        print rightmax

        return res_water


def stringToIntegerList(input):
    return json.loads(input)


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
            height = stringToIntegerList(line)

            ret = Solution().trap(height)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
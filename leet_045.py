import json

class Solution(object):
    def jump_On2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        d = [1000000000] * n
        d[0] = 0
        for i,a in enumerate(nums):
            for s in range(1,a+1):
                if i+s < n:
                    d[i+s] = min(d[i]+1, d[i+s])

        print d
        return d[n-1]

    def jump(self, nums):
        """

        :param nums:
        :return:
        """
        n = len(nums)
        if n==0 or n==1:
            return 0
        istep = 0
        mstep = 0
        last_max = 0
        while istep < n:
            for i in range(last_max, mstep+1):
                if i+nums[i]>mstep:
                    last_max = i
                    mstep = i+nums[i]
            if mstep>=n-1:
                return istep+1
            istep+=1
        return -1

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
            nums = stringToIntegerList(line)

            ret = Solution().jump(nums)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
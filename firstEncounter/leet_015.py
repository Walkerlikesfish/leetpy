import json
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        n = len(nums)
        nums = sorted(nums)
        pa = None
        for ia in range(n-1):
            a = nums[ia]
            if a == pa:
                continue
            ib = ia + 1
            ic = n-1
            while ib < ic:
                b = nums[ib]
                c = nums[ic]
                cur_v = a+b+c
                # print ia,ib,ic
                if cur_v == 0:
                    result.append([a, b, c])
                    while nums[ib] <= b and ib<n-1:
                        ib += 1
                elif cur_v < 0:
                    while nums[ib]<=b and ib<n-1:
                        ib += 1
                else:
                    while nums[ic] >= c and ic>0:
                        ic -= 1
            pa = a

        return result




def stringToIntegerList(input):
    return json.loads(input)


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
            nums = stringToIntegerList(line)

            ret = Solution().threeSum(nums)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
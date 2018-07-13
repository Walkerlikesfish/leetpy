import json

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        O(n^3)
        """
        nums = sorted(nums)
        n = len(nums)
        if n<4:
            return []
        results = []
        pa = 0
        for ia in range(0,n-3):
            a = nums[ia]
            if ia>0 and nums[ia] == nums[pa]:
                pa = ia
                continue
            pa = ia
            pb = ia+1
            for ib in range(ia+1, n-2):
                b = nums[ib]
                if ib>ia+1 and nums[ib] == nums[pb]:
                    pb = ib
                    continue
                pb = ib

                ic = ib+1
                i_d = n-1
                while ic < i_d:
                    c = nums[ic]
                    d = nums[i_d]
                    val = a + b + c + d
                    if val == target:
                        results.append([a, b, c, d])
                        while nums[ic] <= c and ic < i_d:
                            ic += 1
                    elif val < target:
                        while nums[ic] <= c and ic < i_d:
                            ic += 1
                    else:
                        while nums[i_d] >= d and i_d > ic:
                            i_d -= 1
        return results


def stringToIntegerList(input):
    return json.loads(input)


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
            nums = stringToIntegerList(line)
            line = sys.stdin.readline().rstrip('\n')
            target = stringToInt(line)

            ret = Solution().fourSum(nums, target)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
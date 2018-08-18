import json

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 1:
            return [-1,-1]
        self.nums = nums
        self.target = target
        self.resultList = []
        self.binSearch(0, len(nums)-1)
        if len(self.resultList) == 0:
            return [-1,-1]
        return (min(self.resultList), max(self.resultList))

    def binSearch(self,l,r):
        if l<r:
            mid = (l+r)/2
            midv = self.nums[mid]
            if midv > self.target:
                self.binSearch(l, mid-1)
            elif midv < self.target:
                self.binSearch(mid+1, r)
            else: # when we hit the target value
                self.resultList.append(mid)
                self.binSearch(l,mid-1)
                self.binSearch(mid+1,r)
        elif l==r:
            if self.nums[l] == self.target:
                self.resultList.append(l)
            else:
                pass


def stringToIntegerList(input):
    return json.loads(input)


def stringToInt(input):
    return int(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = sys.stdin.readline().strip('\n')
            nums = stringToIntegerList(line)
            line = sys.stdin.readline().strip('\n')
            target = stringToInt(line)

            ret = Solution().searchRange(nums, target)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
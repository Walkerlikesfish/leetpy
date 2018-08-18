# 0 1 2 3 4 5 6 7 8
# 0 1 3 4 5 6 7 8 9
# 7 8 9 0 1 3 4 5 6
# 8 9 0 1 3 4 5 6 7
import json


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.nums = nums
        self.target = target
        if len(nums) < 1:
            return -1
        return self.binSearch(0, len(nums)-1)


    def binSearch(self, l, r):
        if l < r:
            mid = (l+r)/2
            midv = self.nums[mid]
            if self.target == midv:
                return mid
            elif self.target > midv:
                if midv < self.nums[r]: # the right side seq is sorted
                    if self.target <= self.nums[r]:
                        return self.binSearch(mid+1, r)
                    else:
                        return self.binSearch(l, mid-1)
                else: # the left side seq is sorted
                    return self.binSearch(mid+1, r)
            else:
                if midv < self.nums[r]: # the right side seq is sorted
                    return self.binSearch(l, mid-1)
                else: # the left side seq is sorted
                    if self.target >= self.nums[l]:
                        return self.binSearch(l, mid-1)
                    else:
                        return self.binSearch(mid+1, r)
        else:
            if self.nums[l] == self.target:
                return l
            else:
                return -1


def stringToIntegerList(input):
    return json.loads(input)


def stringToInt(input):
    return int(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys

    while True:
        try:
            line = sys.stdin.readline().strip('\n')
            nums = stringToIntegerList(line)
            line = sys.stdin.readline().strip('\n')
            target = stringToInt(line)

            ret = Solution().search(nums, target)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
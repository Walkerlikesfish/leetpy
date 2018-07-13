import json

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        ptr2 = 0
        ptr1 = 0
        cnt1 = 0
        while ptr2 < n and cnt1 < m:
            if nums1[ptr1] < nums2[ptr2]:
                cnt1+=1
                ptr1+=1
            else:
                nums1[ptr1+1:] = nums1[ptr1:-1]
                nums1[ptr1] = nums2[ptr2]
                ptr1+=1
                ptr2+=1

        while ptr2 < n:
            nums1[ptr1] = nums2[ptr2]
            ptr1+=1
            ptr2+=1


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
            line = sys.stdin.readline().rstrip('\n')
            nums1 = stringToIntegerList(line)
            line = sys.stdin.readline().rstrip('\n')
            m = stringToInt(line)
            line = sys.stdin.readline().rstrip('\n')
            nums2 = stringToIntegerList(line)
            line = sys.stdin.readline().rstrip('\n')
            n = stringToInt(line)

            ret = Solution().merge(nums1, m, nums2, n)

            out = integerListToString(nums1)
            if ret is not None:
                print "Do not return anything, modify nums1 in-place instead."
            else:
                print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
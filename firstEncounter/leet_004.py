import json

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # m - larger array -> ind_i
        # n - smaller array -> ind_j
        m = len(nums1)
        n = len(nums2)
        if m > n: # swap two input array if m<n
            nums2, nums1, m, n = nums1, nums2, n, m

        # Deal with one empty array
        if n == 0:
            if m % 2 == 1:
                return nums1[m/2]
            else:
                return float(float(nums1[m/2-1]+nums1[m/2])/2)

        i_min = 0
        i_max = m

        # iterate through the interval linear:
        while i_min<=i_max:
            i_cur = (i_min+i_max)/2
            j_cur = (m+n+1)/2 - i_cur

            if i_cur<m and nums1[i_cur] < nums2[j_cur-1]:
                i_min = i_cur+1

            elif i_cur>0 and nums1[i_cur-1] > nums2[j_cur]:
                i_max = i_cur-1

            else:
                if i_cur == 0:
                    max_of_left = nums2[j_cur-1]
                elif j_cur == 0:
                    max_of_left = nums1[j_cur-1]
                else:
                    max_of_left = max(nums1[i_cur-1], nums2[j_cur-1])

                if (m+n)%2 == 1:
                    return float(max_of_left)
                else:
                    if i_cur == m:
                        min_of_right = nums2[j_cur]
                    elif j_cur == n:
                        min_of_right = nums1[i_cur]
                    else:
                        min_of_right = min(nums1[i_cur], nums2[j_cur])
                    return float((min_of_right+max_of_left))/2


def stringToIntegerList(input):
    return json.loads(input)


def doubleToString(input):
    if input is None:
        input = 0
    return "%.1f" % input


def main():
    import sys
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            nums1 = stringToIntegerList(line)
            line = sys.stdin.readline().rstrip('\n')
            nums2 = stringToIntegerList(line)

            ret = Solution().findMedianSortedArrays(nums1, nums2)
            out = doubleToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
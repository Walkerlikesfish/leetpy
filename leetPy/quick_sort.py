import numpy
import json
import sys


def partition(a, left, right):
    """put a[left] on the right position, and return the index

    :param a:
    :param left:
    :param right:
    :return:
    """
    # exception mark
    if not a or left > right or left < 0 or right >= len(a):
        return -1
    targ = a[left]
    while left < right:
        while a[right] > targ and left < right:
            right -= 1
        a[left] = a[right]
        while a[left] <= targ and left < right:
            left += 1
        a[right] = a[left]
    a[left] = targ
    return left

def quick_sort(nums, left, right):
    if left >= right:
        return
    ind = partition(nums, left, right)
    quick_sort(nums, left, ind-1)
    quick_sort(nums, ind+1, right)


# def partition(a, left, right):
#     """ put the a[left] in to the right position and return the index
#
#     :param a:
#     :param left:
#     :param right:
#     :return:
#         :ind, [int], the index of a[left] in the nums array
#     """
#     # filter the exceptions
#     if not a or left<0 or right>=len(a) or left>right:
#         return -1
#
#     targ = a[left]
#     il = left
#     ir = right
#     while il < ir:
#         while a[ir]>targ and ir>il:
#             ir -= 1
#         a[il] = a[ir]
#         while a[il]<=targ and il<ir:
#             il += 1
#         a[ir] = a[il]
#
#     a[ir] = targ
#
#     return ir
#
#
# def quick_sort(nums, left, right):
#     """quick sort
#
#     :param left:
#     :param right: [int], real pointer, nums[right] has value
#     :param nums:
#     :return:
#     """
#     if left >= right:
#         return
#     ind = partition(nums, left, right)
#     quick_sort(nums, left, ind-1)
#     quick_sort(nums, ind+1, right)


def stringToIntegerList(input):
    return json.loads(input)


def main():
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            nums = stringToIntegerList(line)
            quick_sort(nums,0, len(nums)-1)
            print nums
        except StopIteration:
            break


if __name__ == '__main__':
    main()


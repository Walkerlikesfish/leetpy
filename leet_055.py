import json

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt_step = 0
        n = len(nums)
        last_step = 0
        cur_max_step = 0
        nxt_max_step = 0

        for i in range(0, n):
            if i <= cur_max_step:
                if nums[i]+i >= nxt_max_step:
                    nxt_max_step = nums[i]+i
                    if nxt_max_step >= n:
                        return True
                if i == cur_max_step:
                    cur_max_step = nxt_max_step
                    cnt_step += 1
            else:
                return False

        return True


        # while cur_max_step<n:
        #     for i in range(last_step, cur_max_step+1):
        #         if nums[i]+i > cur_max_step:
        #             cur_max_step = nums[i] + i
        #             if cur_max_step >= n:
        #                 print cnt_step+1
        #                 return True
        #                 break
        #     if last_step == cur_max_step:
        #         return False
        #     cnt_step+=1
        #     last_step = i+1



def stringToIntegerList(input):
    return json.loads(input)


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

            ret = Solution().canJump(nums)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        N_array = []
        while N>0:
            N_array.append(N%10)
            N /= 10
        n_n = len(N_array)
        t_min = pow(10, n_n-1)
        t_max = t_min * 10
        t_map = []
        tmp2 = 1
        while tmp2 <= t_max:
            if tmp2 >= t_min:
                tmp22 = tmp2
                tmp22_array = []
                while tmp22>0:
                    tmp22_array.append(tmp22%10)
                    tmp22 /= 10
                print tmp22_array, N_array
                if sorted(tmp22_array) == sorted(N_array):
                    return True
            tmp2 *= 2
        return False




def stringToInt(input):
    return int(input)


def main():
    import sys
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            N = stringToInt(line)

            ret = Solution().reorderedPowerOf2(N)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        ss_list = list(ss.strip())
        n = len(ss_list)
        permut_candies = [0] * n
        res = []

        def gen_permut(depth, inds):
            if len(inds) >= n:
                print inds
                s = ''
                for ind in inds:
                    s += ss_list[ind]
                res.append(s)
            else:
                for i in range(n):
                    if not permut_candies[i]:
                        permut_candies[i] = 1
                        new_inds = list(inds)
                        new_inds.append(i)
                        gen_permut(depth+1, new_inds)
                        permut_candies[i] = 0

        gen_permut(0, [])
        return sorted(list(set(res)))

    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        tn = len(numbers)
        num_map = {}
        for en in numbers:
            if en not in num_map:
                num_map[en] = 1
            else:
                num_map[en] += 1
            if num_map[en] > tn/2:
                return en
        return 0

    def FindGreatestSumOfSubArray(self, array):
        # write code here
        d = array
        res = 0
        for ia,a in enumerate(array):
            if ia > 0:
                if d[ia-1] > 0:
                    d[ia] = d[ia-1] + a
            if d[ia] > res:
                res = d[ia]
        return res

    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n == 1:
            return 1
        base = 1
        res = 0
        while base<=n:
            a = n/base
            b = n%base + 1
            cur_a = a%10
            # print cur_a, a, b
            if cur_a == 0:
                res += a/10 * base
            elif cur_a == 1:
                res += a/10 * base + b
            else:
                res += (a/10 + 1) * base
            base *= 10
        return res

    def Add(self, num1, num2):
        # write code here
        while num2:
            a = num1 ^ num2  # no carry
            b = num1 & num2  # carry
            if b:
                num1 = a
                num2 = b << 1
            else:
                return a

    def multiply(self, A):
        # write code here
        n = len(A)
        B = [0] * n
        if not A:
            return B
        if n == 1:
            return A
        B[0] = 1
        B[1] = A[0]
        for ix in range(2, n):
            B[ix] = B[ix - 1] * A[ix - 1]

        right = A[n-1]
        for ix in range(n-2, -1, -1):
            B[ix] *= right
            right *= A[ix]

        return B

s = Solution()

input_val = [1,2,3,4,5]
output_val = s.multiply(input_val)
print output_val
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

<<<<<<< HEAD
    def PrintMinNumber(self, numbers):
        def cmp_func(a, b):
            d = int(str(a)+str(b)) - int(str(b)+str(a))
            if d > 0:
                return 1
            elif d < 0:
                return -1
            else:
                return 0
        numbers.sort(cmp=cmp_func)
        res = ''
        for en in numbers:
            res += str(en)
        return res

    def GetUglyNumber_Solution(self, index):
        if index<7:
            return index
        d = [0] * index
        d[0] = 1
        i2, i3, i5 = 0, 0, 0
        for ind in range(1,index):
            d[ind] = min(d[i2]*2, d[i3]*3, d[i5]*5)
            if d[i2]*2 == d[ind]:
                i2 += 1
            if d[i3]*3 == d[ind]:
                i3 += 1
            if d[i5]*5 == d[ind]:
                i5 += 1
        return d[-1]

    def FirstNotRepeatingChar(self, s):
        char_map = {}
        for es in s:
            if es not in char_map:
                char_map[es] = 1
            else:
                char_map[es] += 1
        for ies,es in enumerate(s):
            if char_map[es] == 1:
                return ies

        return -1

    def GetNumberOfK(self, data, k):
        n = len(data)
        lptr = 0
        rptr = n-1
        bl = None
        br = None
        # find left boundary index
        while lptr<rptr:
            midptr = (lptr+rptr)/2
            if data[midptr] >= k:
                rptr = midptr
            else:
                lptr = midptr+1
        if data[lptr] == k:
            bl = lptr
        lptr = 0
        rptr = n-1
        while lptr<rptr:
            midptr = (lptr+rptr+1)/2
            if data[midptr] <= k:
                lptr = midptr
            else:
                rptr = midptr - 1
        if data[rptr] == k:
            br = rptr
        print bl, br
        if bl is not None and br is not None:
            return br - bl + 1
        else:
            return 0

    def LeftRotateString(self, s, n):
        # write code here
        if not s:
            return ""
        s = list(s)
        l = 0
        r = n - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        l = n
        r = len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        l = 0
        r = len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)


s = Solution()

input_val = ("yahaha", 1)
output_val = s.LeftRotateString(input_val[0], input_val[1])
print output_val

'''
class Solution {
public:
    int GetUglyNumber_Solution(int index) {
        if (index < 7)return index;
        vector<int> res(index);
        res[0] = 1;
        int t2 = 0, t3 = 0, t5 = 0, i;
        for (i = 1; i < index; ++i)
        {
            res[i] = min(res[t2] * 2, min(res[t3] * 3, res[t5] * 5));
            if (res[i] == res[t2] * 2)t2++;
            if (res[i] == res[t3] * 3)t3++;
            if (res[i] == res[t5] * 5)t5++;
        }
        return res[index - 1];
    }
};
'''
=======
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
>>>>>>> 12cdb4e5e7ad95c67653c6be107b8808a2481cb5

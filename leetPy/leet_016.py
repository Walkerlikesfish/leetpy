import json


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.results = []
        self.len_digits = len(digits)
        self.digits = digits
        self.phone_dict = {1:[], 2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],
                           7:['p','q','r','s'], 8:['t','u','v'], 9:['w','x','y','z']}
        a = self.cons_strs(0, '')
        return self.results

    def cons_strs(self, cur_ind, cur_str):
        if cur_ind < self.len_digits:
            for s in self.phone_dict[int(self.digits[cur_ind])]:
                cur_str += s
                if cur_ind == self.len_digits - 1:
                    self.results.append(cur_str)
                else:
                    self.cons_strs(cur_ind+1, cur_str)
                cur_str = cur_str[0: cur_ind]


def stringToString(input):
    return input[1:-1].decode('string_escape')

def stringArrayToString(input):
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
            digits = stringToString(line)

            ret = Solution().letterCombinations(digits)

            out = stringArrayToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
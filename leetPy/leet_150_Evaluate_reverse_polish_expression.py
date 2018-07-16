import json

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        st = []
        res = 0
        for et in tokens:
            if et == '/' or et =='*' or et == '+' or et == '-':
                op1 = st.pop()
                op2 = st.pop()
                if et == '/':
                    val = float(float(op2) / op1)
                    val = int(val)
                if et == '*':
                    val = op2 * op1
                if et == '+':
                    val = op2 + op1
                if et == '-':
                    val = op2 - op1
                st.append(val)
                # print val
            else:
                val = int(et)
                st.append(val)
        return st.pop()


def stringToStringArray(input):
    return json.loads(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            tokens = stringToStringArray(line)

            ret = Solution().evalRPN(tokens)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
import json


class TNode(object):
    def __init__(self):
        self.children = {}
        self.flag_end = False


class Trie(object):
    def __init__(self):
        self.head = TNode()

    def insert(self, rootword):
        cur_ptr = self.head
        for each_c in rootword:
            if each_c not in cur_ptr.children:
                cur_ptr.children[each_c] = TNode()
            cur_ptr = cur_ptr.children[each_c]
            if cur_ptr.flag_end:
                break
        cur_ptr.flag_end = True


    def check_sent_word(self, sentword):
        cur_ptr = self.head
        for cc, each_c in enumerate(sentword):
            if each_c in cur_ptr.children:
                cur_ptr = cur_ptr.children[each_c]
            else:
                break
            if cur_ptr.flag_end:
                break
        if cur_ptr.flag_end:
            return sentword[:cc+1]
        else:
            return sentword



class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        t = Trie()
        for each_root in dict:
            t.insert(each_root)
        sent_words = sentence.split()
        res = []
        for each_sent in sent_words:
            res.append(t.check_sent_word(each_sent))
        return ' '.join(res)



def stringToStringArray(input):
    return json.loads(input)


def stringToString(input):
    return input[1:-1].decode('string_escape')


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            dict = stringToStringArray(line)
            line = sys.stdin.readline().rstrip('\n')
            sentence = stringToString(line)

            ret = Solution().replaceWords(dict, sentence)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
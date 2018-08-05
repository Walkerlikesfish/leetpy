import json

class TNode(object):
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None
        self.iw = None


def is_hw(word):
    if not word:
        return False
    if len(word) == 1:
        return True
    left = 0
    right = len(word)-1
    while left <= right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True


class Trie(object):
    def __init__(self):
        self.head = TNode()

    def insert_word(self, word, iw):
        cur_ptr = self.head
        for each_c in word:
            if each_c not in cur_ptr.children:
                cur_ptr.children[each_c] = TNode()
            cur_ptr = cur_ptr.children[each_c]
        cur_ptr.is_word = True
        cur_ptr.word = word
        cur_ptr.iw = iw

    def search_and_return_pard(self, word):
        res = []
        cur_ptr = self.head
        for ic, each_c in enumerate(word):
            if cur_ptr.is_word: # found one possible
                cand = word[ic:]
                if is_hw(cand) and cur_ptr.iw not in res:
                    res.append(cur_ptr.iw)
            if each_c in cur_ptr.children:
                cur_ptr = cur_ptr.children[each_c]
            else:
                if not cur_ptr.children: # exhausted dict
                    cand = word[ic:]
                    if is_hw(cand) and cur_ptr.iw not in res:
                        res.append(cur_ptr.iw)
                    return res
                else:
                    return res
        # word is exhausted
        n_word = len(word)
        if cur_ptr.is_word:
            res.append(cur_ptr.iw)

        # check if the rest of the Trie can give a hw
        sq = [cur_ptr]
        hptr = 0
        while hptr<len(sq):
            cur_ptr = sq[hptr]
            if cur_ptr.is_word:
                if is_hw(cur_ptr.word[n_word:]):
                    res.append(cur_ptr.iw)
            for each_child in cur_ptr.children:
                sq.append(cur_ptr.children[each_child])
            hptr += 1

        return res


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        if not words:
            return []
        self.res = []
        # init the Trie
        self.t = Trie()
        for iw,each_word in enumerate(words):
            self.t.insert_word(each_word, iw)
        # search the pair, looking for who is appropriate to append
        for iw,each_word in enumerate(words):
            r_word = each_word[::-1]
            tmp = self.t.search_and_return_pard(r_word)
            for et in tmp:
                if et != iw:
                    self.res.append([et, iw])
        return self.res

def stringToStringArray(input):
    return json.loads(input)


def int2dArrayToString(input):
    return json.dumps(input)


def main():
    import sys

    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            words = stringToStringArray(line)

            ret = Solution().palindromePairs(words)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
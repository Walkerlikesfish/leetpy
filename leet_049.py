import json

class Solution(object):
    def groupAnagrams_TLE(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        nstrs = len(strs)
        str_hash = []
        results = []
        for each_str in strs:
            cur_dict = {}
            for c in each_str:
                try:
                    cur_dict[c]+=1
                except KeyError:
                    cur_dict[c] = 1
            found = False
            for ind, each_hash in enumerate(str_hash):
                if cmp(cur_dict, each_hash) == 0:
                    found = True
                    results[ind].append(each_str)
                    break
            if not found:
                str_hash.append(cur_dict)
                results.append([each_str])
        return results

    def groupAnagrams(self, strs):
        strsc = list(strs)
        cur_map = {}
        for ind,each_str in enumerate(strs):
            cur_str = "".join(sorted(each_str))
            if cur_str not in cur_map:
                cur_map[cur_str] = [strsc[ind]]
            else:
                cur_map[cur_str].append(strsc[ind])
        result = []
        for each_key in cur_map:
            result.append(cur_map[each_key])
        return result


def stringToStringArray(input):
    return json.loads(input)


def string2dArrayToString(input):
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
            strs = stringToStringArray(line)

            ret = Solution().groupAnagrams(strs)

            out = string2dArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
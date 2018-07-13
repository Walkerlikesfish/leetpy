# Definition for a binary tree node.
import json
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        else:
            imid = len(nums)/2
            root = TreeNode(nums[imid])
            root.left = self.sortedArrayToBST(nums[0:imid])
            root.right = self.sortedArrayToBST(nums[imid+1:])
            return root


def stringToIntegerList(input):
    return json.loads(input)


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


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

            ret = Solution().sortedArrayToBST(nums)

            out = treeNodeToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()
# leetleet
A repo host the leetcode oj solutions.

## Categories

### Simple Questions

### Dynamic Programming
- contest 137-4: 从序列中任意合并两个石头，最后序列剩余一个石头，求最后剩余的量的最小值。

### Tree Related

### DFS / BFS

### System Design


## Details
### Contest 137-4
#### Descriptioin
Each turn, we choose any two rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the smallest possible weight of this stone (the weight is 0 if there are no stones left.)

#### Notes
First Try: It is not possible to be done in DFS/BFS brutal force search, then what should we do...
=> Abstraction / extract the rules from abstraction:
just enumerate from 3,4 examples, do not use numbers but algebra samples. `Write a sequeece (7,4,1,5) -> (a,b,c,d)` Then you may find out: It is infact trying to find the minimum of two groups of numbers.
Then we can use DP to design the algorithm.

#### Code
```python3
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {0}
        sums = 0
        for istone in stones:
            sums += istone
            dp |= {istone + i for i in dp}
        
        res = 100
        for iv in dp:
            res = min(res, abs(sums - 2*iv))
        
        return res
```
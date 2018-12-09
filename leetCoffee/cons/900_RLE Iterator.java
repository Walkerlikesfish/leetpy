/*
con101 900. RLE Iterator
Write an iterator that iterates through a run-length encoded sequence.

The iterator is initialized by RLEIterator(int[] A), where A is a run-length encoding of some sequence.  More specifically, for all even i, A[i] tells us the number of times that the non-negative integer value A[i+1] is repeated in the sequence.

The iterator supports one function: next(int n), which exhausts the next n elements (n >= 1) and returns the last element exhausted in this way.  If there is no element left to exhaust, next returns -1 instead.

For example, we start with A = [3,8,0,9,2,5], which is a run-length encoding of the sequence [8,8,8,5,5].  This is because the sequence can be read as "three eights, zero nines, two fives".
 */
// sol 2
class RLEIterator {

    private int[] B;
    private int ptrTimes;
    private int curTimes;

    public RLEIterator(int[] A) {
        B = A.clone();
        ptrTimes = 0;
        curTimes = 0;
    }

    public int next(int n) {
        if (ptrTimes > B.length-2) return -1;
        int ret = -1;
        if (curTimes + n <= B[ptrTimes]) {
            ret = B[ptrTimes + 1];
            curTimes += n;
        } else {
            int tmpTimes = curTimes + n;
            while (ptrTimes <= B.length - 2 && B[ptrTimes] < tmpTimes) {
                tmpTimes -= B[ptrTimes];
                ptrTimes += 2;
            }
            if (ptrTimes > B.length - 2) {
                return -1;
            }
            curTimes = tmpTimes;
            // ptrTimes <= B.length - 2, B[ptrTimes] >= curTimes
            ret = B[ptrTimes + 1];
        }
        return ret;
    }
}

/**
 * Your RLEIterator object will be instantiated and called as such:
 * RLEIterator obj = new RLEIterator(A);
 * int param_1 = obj.next(n);
 */

// sol 1, blunt
class RLEIterator {

    private List<Integer> list;
    private int cur;

    public RLEIterator(int[] A) {
        list = new ArrayList<>();
        int i = 0;
        int times = 0;
        while (i < A.length) {
            if (i % 2 == 0) {
                if (A[i] == 0) {
                    i += 2;
                    continue;
                }
                times = A[i];
            } else {
                for (int j = 0; j < times; j++) {
                   list.add(A[i]);
                }
            }
            i++;
        }

        cur = 0;
    }

    public int next(int n) {
        if ((cur + n) > list.size()) {
            cur += n;
            return -1;
        }
        else {
            int ret = list.get(cur + n - 1);
            cur += n;
            return ret;
        }
    }
}

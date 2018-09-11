class Solution {
    public int countPrimes(int n) {
        // we cannot go ahead and check every number < n and see if prime,
        // too much redundant work
        // instead, we check the multiples of numbers < sqrt(n) as non prime,
        // so that the numbers left are primes.
        if (n <= 1) return 0;
        int sqrt = (int) Math.sqrt(n) + 1;
        int res = 0;
        boolean[] k = new boolean[n+1];
        Arrays.fill(k, true);
        k[1] = false;
        for (int i = 2; i <= sqrt; i++) {
            // if i is a prime itself
            if (k[i]) {
                // multiples from i, stepping by i
                for (int j = i * i; j < n; j += i) {
                    k[j] = false;
                }
            }
        }
        for (int i = 2; i < n; i++) {
            if (k[i]) res++;
        }
        return res;
    }
}

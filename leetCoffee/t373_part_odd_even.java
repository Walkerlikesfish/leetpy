public class Solution {
    /*
     * @param nums: an array of integers
     * @return: nothing
     */
    public void partitionArray(int[] nums) {
        // not maintaining order
        /*
        int odd = 0, even = nums.length - 1;
        while (odd < even) {
            while (odd < even && (nums[odd] % 2 !=0 )) {
                odd++;
            }
            while (odd < even && (nums[even] % 2 ==0 )) {
                even--;
            }
            if (odd < even) {
                swap(nums, odd, even);
                odd++;
                even--;
            }
        }
        */
        
        // maintaining order
        int i = 0;
        while (i < nums.length) {
            if (nums[i] % 2 != 0) {
                int j = i, k = j - 1;
                while (k >= 0 && nums[k] % 2 == 0) {
                    swap(nums, j, k);
                    k--;
                    j--;
                } 
            }
            i++;
            
        }
        
    }
    
    private void swap(int[] nums, int a, int b) {
        int tmp = nums[b];
        nums[b] = nums[a];
        nums[a] = tmp;
    }
}

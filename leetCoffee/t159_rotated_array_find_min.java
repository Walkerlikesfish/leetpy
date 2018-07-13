public class Solution {
    /**
     * @param nums: a rotated sorted array
     * @return: the minimum number in the array
     */
    public int findMin(int[] nums) {
        if (nums == null || nums.length == 0) return -1;
        int start = 0, len = nums.length, end = len - 1, mid;
        
        if (nums[start] < nums[end]) return nums[start];
        
        while (start + 1 < end) {
            mid = (end + start) / 2;
            if (nums[mid] > nums[start]) {
                start = mid;
            } else {
                end = mid;
            }
        }
        
        if (nums[start] < nums[end]) return nums[start];
        else if (nums[start] > nums[end]) return nums[end];
        return -1;
    }
}

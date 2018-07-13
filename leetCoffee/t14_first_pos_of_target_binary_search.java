public class Solution {
    /**
     * @param nums: The integer array.
     * @param target: Target to find.
     * @return: The first position of target. Position starts from 0.
     */
     
    /*
     // Wrong solution: cannot handle duplicate, need more runs in the loop
     // Key Point: there might be duplicates, you just need to narrow down the front half and be precise.
    
    public int binarySearch(int[] nums, int target) {
        if (nums == null || nums.length == 0) return -1;
        int start = 0, end = 0, mid = 0, length = nums.length;
        end = length - 1;
        mid = end / 2;
        while (start + 1 < end) {
            if (nums[mid] == target) {
                return mid;
            }
            if (nums[mid] < target) {
                start = mid;
            }
            if (nums[mid] > target) {
                end = mid;
            }
            mid = (start + end) / 2;
        }
        if (nums[start] == target) {
            return start;
        }
        if (nums[end] == target) {
            return end;
        }
        return -1;
    }
     */ 
     
    /* correct
    public int binarySearch(int[] nums, int target) {
        if (nums == null || nums.length == 0) return -1;
        int start = 0, end = 0, mid = 0, length = nums.length;
        end = length - 1;
        while (start + 1 < end) {
            mid = (start + end) / 2;
            if (nums[mid] < target) {
                start = mid;
            }
            else {
                end = mid;
            }
        }
        if (nums[start] == target) {
            return start;
        }
        if (nums[end] == target) {
            return end;
        }
        return -1;
    }
    */


    // recursion: slow
    public int binarySearch(int[] nums, int target) {
        //write your code here
        if(nums == null || nums.length == 0)
        	return -1;
       	int start = 0, end = nums.length-1;

       	return bsRecursion(nums, target, start, end);

    }

    public int bsRecursion(int[] nums, int target, int start, int end) {
    	int mid = start + (end - start)/2;
    	if(start+1 < end) {
    		if(nums[mid] == target)
	    		return bsRecursion(nums, target, start, mid);
	    	else if(nums[mid] < target)
	    		return bsRecursion(nums, target, mid, end);
	    	else if(nums[mid]>target)
	    		return bsRecursion(nums, target, start, mid);
    	} else {
    		if(nums[start] == target)
    			return start;
    		if(nums[end]   == target)
    			return end;
    	}
    	return -1;

    }
}

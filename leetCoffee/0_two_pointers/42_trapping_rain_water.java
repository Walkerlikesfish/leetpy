/*
 Sol: two pointer
 Always moves forward
 */
class Solution {
    public int trap(int[] height) {
        int len = height.length;
        if (len <= 1) return 0;
        int left = 0, right = len - 1, water = 0, lefth = height[left], righth = height[right];
        while (left < right) {
            if (height[left] < height[right]) {
                left++;
                if (height[left] < lefth) {
                    water += lefth - height[left];
                } else {
                    lefth = height[left];
                }
            } else {
                right--;
                if (height[right] < righth) {
                    water += righth - height[right];
                } else {
                    righth = height[right];
                }
            }
        }
        return water;
    }
}

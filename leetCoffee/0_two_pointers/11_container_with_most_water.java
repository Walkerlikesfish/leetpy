/*
 Sol 1:
 Idea:
 directly calculates area
  go with left {
    if left pointer fails to enlarge area, left goes back to former point (did not get better)
    if succeeds, keep it
  }
  right {
    if succeeds, keep it
    if right pointer fails to enlarge area, right goes back to former point (did not get better)
      in this case if left pointer fails to enlarge area either, then move right pointer just to move forward (we can move left pointer too, but only one of them)
  }

 */
class Solution {
    public int maxArea(int[] height) {

        int len = height.length;
        if (len <= 1) {
            return 0;
        }
        int left = 0, right = len - 1, area = 0;
        area = Math.min(height[left], height[right]) * (right - left);
        while (left < right) {
            int curArea = area;

            int preLeft = left;
            boolean leftSuccess = false;
            while (left < right && curArea <= area) {
                left++;
                curArea = Math.min(height[left], height[right]) * (right - left);
            }
            if (curArea > area) {
                area = curArea;
                leftSuccess = true;
            } else {
                left = preLeft;
            }
            int preRight = right;
            while (left < right && curArea <= area) {
                right--;
                curArea = Math.min(height[left], height[right]) * (right - left);
            }
            if (curArea > area) {
                area = curArea;
            } else {
                right = preRight;
                if (!leftSuccess) {
                    // left & right both failed, move forward
                    right = preRight;
                    //left++;
                    right--;
                }
            }
        }
        return area;
    }
}

/*
 Sol 2
  Traverse, always move foward and hope for the best
  Compare left and right heights (only higher heights will possibly lead to a better result)
  Simple loop body
 */
 class Solution {
    public int maxArea(int[] height) {

        int len = height.length;
        if (len <= 1) {
            return 0;
        }
        int left = 0, right = len - 1, area = 0;
        while (left < right) {
            area = Math.max(area, Math.min(height[left], height[right]) * (right - left));
            if (height[left] < height[right]) {
                // keeping left where it was will not help
                left++;
            } else {
                right--;
            }
        }
        return area;
    }
}

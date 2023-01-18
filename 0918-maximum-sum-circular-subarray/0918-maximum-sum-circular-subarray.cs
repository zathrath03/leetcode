public class Solution {
    public int MaxSubarraySumCircular(int[] nums) {
        int total, curMax, curMin, maxSum, minSum;
        total = curMax = curMin = 0;
        maxSum = minSum = nums[0];
        foreach (var num in nums){
            curMax = num > num + curMax ? num : num + curMax;
            maxSum = curMax > maxSum ? curMax : maxSum;
            curMin = num < num + curMin ? num : num + curMin;
            minSum = curMin < minSum ? curMin : minSum; 
            total += num;
        }
        return maxSum > 0 ? Math.Max(maxSum, total - minSum) : maxSum;
    }
}
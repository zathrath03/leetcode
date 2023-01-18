public class Solution {
    public int MaxSubarraySumCircular(int[] nums) {
        int total, curMax, curMin, maxSum, minSum;
        total = curMax = curMin = 0;
        maxSum = minSum = nums[0];
        foreach (var num in nums){
            curMax = Math.Max(num, num + curMax);
            maxSum = Math.Max(curMax, maxSum);
            curMin = Math.Min(num, num + curMin);
            minSum = Math.Min(curMin, minSum);
            total += num;
        }
        return maxSum > 0 ? Math.Max(maxSum, total - minSum) : maxSum;
    }
}
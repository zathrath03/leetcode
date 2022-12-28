public class Solution {
    public int MinStoneSum(int[] piles, int k) {
        var maxHeap = new PriorityQueue<int,int>(piles.Select(p => (p, -p)));
        int sum = piles.Sum();
        for (int _ = 0; _ < k; _++)
        {
            int largestPile = maxHeap.Peek();
            int halfOfLargestPile = largestPile / 2;
            sum -= halfOfLargestPile;
            int p = largestPile - halfOfLargestPile;

            maxHeap.EnqueueDequeue(p, -p);
        }
        return sum;
    }
}
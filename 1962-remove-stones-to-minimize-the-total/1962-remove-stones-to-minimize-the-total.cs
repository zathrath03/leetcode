public class Solution {
    public int MinStoneSum(int[] piles, int k) {
        var maxHeap = new PriorityQueue<int,int>(piles.Select(p => (p, -p)));
        int sum = piles.Sum();
        for (int _ = 0; _ < k; _++)
        {
            int halfOfLargestPile = maxHeap.Peek() / 2;
            sum -= halfOfLargestPile;
            int p = maxHeap.Dequeue() - halfOfLargestPile;

            maxHeap.Enqueue(p, -p);
        }
        return sum;
    }
}
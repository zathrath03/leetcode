public class Solution {
    public int MaxIceCream(int[] costs, int coins) {
        Array.Sort(costs);
        var count = 0;

        foreach (var cost in costs){
            coins -= cost;
            if (coins < 0) break;
            count += 1;
        }

        return count;
    }
}
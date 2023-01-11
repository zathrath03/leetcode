public class Solution {
    public long MinimumHealth(int[] damage, int armor) {
        var maxDamage = damage.Aggregate(0L, (sum, dmg) => sum + dmg);
        return 1 + maxDamage - Math.Min(damage.Max(), armor);
    }
}
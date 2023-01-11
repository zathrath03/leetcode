public class Solution {
    public long MinimumHealth(int[] damage, int armor) {
        long totalDamage = 0;
        var maxDamageSeen = 0;

        foreach (var d in damage) {
            maxDamageSeen = Math.Max(d, maxDamageSeen);
            totalDamage += d;
        }

        return 1 + totalDamage - Math.Min(armor, maxDamageSeen);
    }
}
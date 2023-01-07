public class Solution {
    public int CanCompleteCircuit(int[] gas, int[] cost) {
        var start = 0;
        var running_sum = 0;
        var total_sum = 0;

        for (int i = 0; i < gas.Length; i++){
            var excess_gas = gas[i] - cost[i];
            total_sum += excess_gas;
            running_sum += excess_gas;
            if (running_sum < 0){
                running_sum = 0;
                start = i + 1;
            }
        }
        return total_sum >= 0 ? start : -1;
    }
}
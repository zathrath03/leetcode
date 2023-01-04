public class Solution {
    public int MinimumRounds(int[] tasks) {
        var taskCounts = new Dictionary<int, int>();
        
        foreach( var task in tasks ) {
            if (taskCounts.TryGetValue(task, out int count)) {
                taskCounts[task] = ++count;
            } else {
                taskCounts.Add(task, 1);
            }
        }
        
        int rounds = 0;
        
        foreach( int count in taskCounts.Values) {
            if( count == 1 ) return -1;
            rounds += count / 3;
            int rem = count % 3;
            if( rem > 0 ) {
                rounds += 1;
            }
        }
        
        return rounds;
    }
}
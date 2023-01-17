public class Solution {
    public int MinFlipsMonoIncr(string s) {
        int flipCount = 0;
        int onesCount = 0;
        
        foreach (var c in s) {
            if (c == '1')
                onesCount++;
            else if (onesCount > flipCount)
                flipCount++;
        }
        return flipCount;
    }
}
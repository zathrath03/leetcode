impl Solution {
    pub fn min_flips_mono_incr(s: String) -> i32 {
        let mut flip_count = 0;
        let mut ones_count = 0;
        
        for c in s.chars() {
            if c == '1' {
                ones_count += 1
            }
            else if ones_count > flip_count {
                flip_count += 1
            }
        }
        flip_count
    }
}
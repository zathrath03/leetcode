impl Solution {
    pub fn min_flips_mono_incr(s: String) -> i32 {
        s.chars()
            .fold((0, 0), |(ones, x), c| match c {
                '0' => (ones, ones.min(x + 1)),
                _ => (ones + 1, x),
            })
            .1
    }
}
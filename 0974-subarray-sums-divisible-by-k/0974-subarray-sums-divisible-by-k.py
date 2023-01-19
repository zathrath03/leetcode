class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = prefix = 0
        mods = [1] + [0] * (k - 1)
        
        for num in nums:
            prefix = (prefix + num) % k
            count += mods[prefix]
            mods[prefix] += 1
        
        return count
class Solution:
    def earliestFullBloom(self, plantTime: List[int],
                          growTime: List[int]) -> int:
        cur_plant_time = 0
        output = 0
        indices = sorted(range(len(plantTime)), key=lambda x: growTime[x], reverse = True) 
        for i in indices:
            cur_plant_time += plantTime[i]
            output = max(output, cur_plant_time + growTime[i])
        return output

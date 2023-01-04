class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        task_counts = Counter(tasks)
        
        rounds = 0
        for count in task_counts.values():
            if count == 1:
                return -1
            additional_rounds, count = divmod(count, 3)
            rounds += additional_rounds
            if count > 0:
                rounds += 1
        return rounds    
                
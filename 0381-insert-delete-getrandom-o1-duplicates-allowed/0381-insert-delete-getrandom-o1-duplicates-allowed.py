class RandomizedCollection:

    def __init__(self):
        self.item_position_map = defaultdict(list)
        self.items = []

    def insert(self, val: int) -> bool:
        is_not_present = val not in self.item_position_map
        self.item_position_map[val].append(len(self.items))
        self.items.append(val)
        return is_not_present

    def remove(self, val: int) -> bool:
        if (is_present := val in self.item_position_map):
            positions = self.item_position_map[val]
            if len(positions) == 1:
                position = positions[0]
                del self.item_position_map[val]
            else:
                position = positions.pop()
            last_item = self.items.pop()
            if  position != len(self.items):
                self.items[position] = last_item
                self.item_position_map[last_item][-1] = position
                self.item_position_map[last_item].sort()
        return is_present

    def getRandom(self) -> int:
        return random.choice(self.items)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
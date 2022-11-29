class RandomizedSet:

    def __init__(self):
        self.item_position_map = {}
        self.items = []

    def insert(self, val: int) -> bool:
        if val in self.item_position_map:
            return False
        self.items.append(val)
        self.item_position_map[val] = len(self.items) - 1
        return True

    def remove(self, val: int) -> bool:
        try:
            position = self.item_position_map.pop(val)
            last_item = self.items.pop()
            if position != len(self.items):
                self.items[position] = last_item
                self.item_position_map[last_item] = position
            return True
        except KeyError:
            return False

    def getRandom(self) -> int:
        return random.choice(self.items)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
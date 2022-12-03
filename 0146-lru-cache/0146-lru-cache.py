class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.q = deque()

    def get(self, key: int) -> int:
        value = self.cache.get(key, -1)
        if value != -1:
            self.q.remove(key)
            self.q.append(key)
        return value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                to_remove = self.q.popleft()
                del self.cache[to_remove]
        else:
            self.q.remove(key)
        self.cache[key] = value
        self.q.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
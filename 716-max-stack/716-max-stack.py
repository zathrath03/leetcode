from heapq import heapify, heappush, heappop

class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_map = []
        self.removed = set()
        self.ctr = 0
        

    def push(self, x: int) -> None:
        self.stack.append((x, self.ctr))
        heappush(self.max_map, (-x, -self.ctr))
        self.ctr += 1


    def pop(self) -> int:
        x, ctr = self.stack.pop()
        while ctr in self.removed:
            self.removed.remove(ctr)
            x, ctr = self.stack.pop()
        self.removed.add(ctr)
        return x

    
    def top(self) -> int:
        while self.stack[-1][1] in self.removed:
            self.removed.remove(self.stack[-1][1])
            del self.stack[-1]
        return self.stack[-1][0]

    
    def peekMax(self) -> int:
        while self.max_map[0][1] * -1 in self.removed:
            self.removed.remove(self.max_map[0][1] * -1)
            heappop(self.max_map)
        return self.max_map[0][0] * -1

    
    def popMax(self) -> int:
        neg_x, neg_ctr = heappop(self.max_map)
        while neg_ctr * -1 in self.removed:
            self.removed.remove(neg_ctr * -1)
            neg_x, neg_ctr = heappop(self.max_map)
        self.removed.add(neg_ctr * -1)
        return neg_x * -1


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
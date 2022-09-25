class MyCircularQueue:

    def __init__(self, k: int):
        self.front = self.rear = None
        self.len = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.len == self.capacity:
            return False
        if not self.front:
            self.front = self.rear = Node(value)
        else:
            self.rear.next = Node(value)
            self.rear = self.rear.next
        self.len += 1
        return True

    def deQueue(self) -> bool:
        if not self.front:
            return False
        if self.len == 1:
            self.front = self.rear = None
        else:
            self.front = self.front.next
        self.len -= 1
        return True

    def Front(self) -> int:
        if self.front:
            return self.front.data
        return -1

    def Rear(self) -> int:
        if self.rear:
            return self.rear.data
        return -1

    def isEmpty(self) -> bool:
        return not self.len

    def isFull(self) -> bool:
        return self.len == self.capacity


class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

class MyStack:

    def __init__(self):
        self.queue = deque()
        self.reversedQueue = deque()

    def push(self, x: int) -> None:
        while self.reversedQueue:
            self.queue.append(self.reversedQueue.popleft())
        self.queue.append(x)


    def pop(self) -> int:
        if self.reversedQueue:
            while len(self.reversedQueue) != 1:
                self.queue.append(self.reversedQueue.popleft())
            return self.reversedQueue.popleft()
        if self.queue:
            while len(self.queue) != 1:
                self.reversedQueue.append(self.queue.popleft())
            return self.queue.popleft()
            

    def top(self) -> int:
        if self.reversedQueue:
            while len(self.reversedQueue) != 1:
                self.queue.append(self.reversedQueue.popleft())
            ans = self.reversedQueue.popleft()
            self.queue.append(ans)
        if self.queue:
            while len(self.queue) != 1:
                self.reversedQueue.append(self.queue.popleft())
            ans = self.queue.popleft()
            self.reversedQueue.append(ans)
        return ans
        

    def empty(self) -> bool:
        return not self.queue and not self.reversedQueue
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
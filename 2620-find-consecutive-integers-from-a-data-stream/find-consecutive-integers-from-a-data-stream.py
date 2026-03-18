class DataStream:

    def __init__(self, value: int, k: int):
        self.DataStream = deque()
        self.check = value
        self.window = k
        self.count = 0

    def consec(self, num: int) -> bool:
        self.DataStream.append(num)
        if num == self.check:
            self.count += 1
        if len(self.DataStream)>self.window:
            removed = self.DataStream.popleft()
            if removed == self.check:
                self.count -= 1
        return self.count >= self.window


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
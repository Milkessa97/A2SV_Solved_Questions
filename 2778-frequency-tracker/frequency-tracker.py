class FrequencyTracker:

    def __init__(self):
        self.FrequencyTracker = defaultdict(int)
        self.track = defaultdict(int)
    def add(self, number: int) -> None:
        old = self.track[number]
        new = old + 1
        self.track[number] = new
        if old > 0:
            self.FrequencyTracker[old] -= 1
        self.FrequencyTracker[new] += 1

    def deleteOne(self, number: int) -> None:
        if self.track[number] == 0:
            return
        old = self.track[number]
        new = old - 1
        self.FrequencyTracker[old] -= 1
        if new > 0:
            self.FrequencyTracker[new] += 1
        self.track[number] = new

    def hasFrequency(self, frequency: int) -> bool:
        return self.FrequencyTracker[frequency] > 0    


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
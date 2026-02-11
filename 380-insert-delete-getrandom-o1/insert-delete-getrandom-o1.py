class RandomizedSet:

    def __init__(self):
        self.random = set()

    def insert(self, val: int) -> bool:
        if val in self.random:
            return False
        else:      
            self.random.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.random:
            self.random.remove(val)
            return True
        else:      
            return False

    def getRandom(self) -> int:
        tup = tuple(self.random)
        return random.choice(tup)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
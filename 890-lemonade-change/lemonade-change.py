class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = defaultdict(int)
        for bill in bills:
            count[bill] += 1
            if bill == 10:
                if 5 in count:
                    count[5] -= 1
                else:
                    return False
            if bill == 20:
                if 5 in count and 10 in count:
                        count[5] -= 1
                        count[10] -= 1
                elif 5 in count and count[5] > 2:
                    count[5] -= 3
                else:
                    return False
            if count[5] == 0:
                del count[5]
            if count[10] == 0:
                del count[10]
            print(count)
        return True 
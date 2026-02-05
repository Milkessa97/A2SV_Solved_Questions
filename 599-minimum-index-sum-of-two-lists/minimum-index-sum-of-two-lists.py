class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_value = float('inf')
        res = []
        for idx,word in enumerate(list1):
            for index,value in enumerate(list2):
                if word == value:
                    if min_value > idx+index:
                        min_value =  idx+index
                        res = [value]
                    elif min_value == idx+index:
                        res.append(value)
        return res
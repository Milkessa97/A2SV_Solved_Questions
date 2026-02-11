class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        first_elt = num // 3

        while first_elt*3 + 3 >= num:
            if first_elt*3 + 3 ==  num:
                return [first_elt, first_elt + 1, first_elt + 2]

            elif first_elt*3 + 3 < num:
                return []
                
            first_elt -= 1
        return []
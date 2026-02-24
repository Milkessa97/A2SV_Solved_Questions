class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left,right = 0, len(people) - 1
        boats = 0

        while left<=right:
            if people[right] + people[right-1] <= limit:
                boats += 1
                right -= 2

            elif people[right] + people[left] <= limit:
                boats += 1
                right -= 1
                left += 1

            else:
                boats += 1
                right -= 1
                
        return boats
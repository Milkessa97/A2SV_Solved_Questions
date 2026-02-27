class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left,right = 0, len(skill)-1
        total_chemistry = 0
        check = skill[left]+skill[right]

        while left<right:
            chemistry = skill[left]*skill[right]
            total_chemistry += chemistry

            if skill[left] + skill[right] != check:
                return -1

            right -= 1
            left += 1
        return total_chemistry

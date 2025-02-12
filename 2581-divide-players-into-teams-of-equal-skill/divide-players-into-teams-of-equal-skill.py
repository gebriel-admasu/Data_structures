class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left,right = 0,len(skill)-1
        target = skill[left] + skill[right]
        skill_sum =0
        while left <= right:
            if skill[left] + skill[right] == target:
                mult_skill = skill[left]*skill[right]
                skill_sum +=mult_skill

                right -=1
                left +=1
            else:
                return -1
        return skill_sum
"""
https://leetcode.com/problems/reach-a-number/

Sol:
jump and till target or cross target
if cross target and position(diff) is  even that means , its equal to jum return count
else jump more and ans  njot found that mean count + 1 will be answer
odd + odd = even

"""

class Solution:
    def reachNumber(self, target: int) -> int:
        i = 0
        jump = 1
        count = 0
        target = abs(target)
        while i < target:
            i+=jump
            jump+=1
            count+=1
            if i == target:
                return count
        position = target - i 
        if position%2 == 0:
            return count
        else:
            #one more jump annd check diff for odd even
            #if even then count is answer else one more jump and check odd even
            # adn diff is even then count is answer , if diff is again odd that means next diff is going to gurnteed even so count +1 is answer
            i+=jump
            jump+=1
            count+=1
            position = target - i
            if position%2 == 0:
                return count
            else:
                return count+1
            
    

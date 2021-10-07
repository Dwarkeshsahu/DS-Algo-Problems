"""
https://leetcode.com/problems/boats-to-save-people/


sort and move from both left and right or just right side
"""

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people)-1
        count = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left+=1
                right-=1
            else:
                right-=1
            count+=1
        return count



# class Solution:
#     def numRescueBoats(self, people: List[int], limit: int) -> int:
#         people.sort()
#         left = 0
#         right = len(people)-1
#         count = 0
#         while left <= right:
#             if people[left] + people[right] <= limit:
#                 left+=1
#                 right-=1
#             elif people[left] > people[right]:
#                 left+=1
#             else:
#                 right-=1
#             count+=1
#         return count
                
                

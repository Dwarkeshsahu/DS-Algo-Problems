"""
https://leetcode.com/problems/valid-palindrome-ii/

"""


class Solution:
    def isPalindrome(self,s, start , end):
        while start < end:
            if s[start] == s[end]:
                start+=1
                end-=1
            else:
                return False
        return True
    
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] == s[right]:
                left+=1
                right-=1
            else:
                return self.isPalindrome(s, left+1 , right) or self.isPalindrome(s, left , right-1)
        return True
                        
                

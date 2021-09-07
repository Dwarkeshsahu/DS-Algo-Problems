"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s)-1
        vowels = {'a', 'e', 'i','o','u', 'A', 'E', 'I','O','U'}
        s = [x for x in s]
        while left < right:
            if s[left] not in vowels:
                left+=1
            if s[right] not in vowels:
                right-=1
            if s[left] in vowels and s[right] in vowels:
                s[left] , s[right] = s[right], s[left]
                left+=1
                right-=1
        return ''.join(s)

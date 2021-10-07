"""
https://leetcode.com/problems/partition-labels/


make frequency map and loop for each ch max range
"""
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hmap = {}
        for i in range(len(s)):
            if s[i] not in hmap:
                hmap[s[i]] = 0
            hmap[s[i]] = i

        maxx = float("-inf")
        start = 0
        res = []
        for i in range(len(s)):
            maxx = max(hmap[s[i]], maxx)
            if i == maxx:
                res.append(i- start+1)
                start = i+1
                
        return res
        
